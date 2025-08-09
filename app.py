import discord
from discord.ext import commands, tasks
import os
import traceback
from flask import Flask
import sys
import aiohttp
import asyncio
from dotenv import load_dotenv
import threading
import logging
import signal
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize environment variables
load_dotenv()

# Flask Setup
app = Flask(__name__)
bot_name = "Loading..."

@app.route('/')
def home():
    """Health check endpoint for Render"""
    return f"Bot {bot_name} is operational"

@app.route('/health')
def health():
    """Health check endpoint for Render"""
    return {"status": "healthy", "bot": bot_name}

def run_flask():
    """Run Flask with Render-compatible settings"""
    try:
        port = int(os.environ.get("PORT", 10000))
        # Use waitress for production instead of Flask's development server
        from waitress import serve
        serve(app, host='0.0.0.0', port=port, threads=1)
    except Exception as e:
        logger.error(f"Flask server error: {e}")

# Discord Bot Setup
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Missing TOKEN in environment")

class Bot(commands.Bot):
    def __init__(self):
        # Configure minimal required intents
        intents = discord.Intents.default()
        intents.message_content = True
        
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )
        self.session = None
        self.start_time = time.time()
        self._shutdown = False

    async def setup_hook(self):
        """Initialize bot components"""
        try:
            # Create a single session for the entire bot
            connector = aiohttp.TCPConnector(limit=10, limit_per_host=5)
            self.session = aiohttp.ClientSession(connector=connector)
            
            # Load cogs
            try:
                await self.load_extension("cogs.infoCommands")
                logger.info("✅ Successfully loaded InfoCommands cog")
            except Exception as e:
                logger.error(f"❌ Failed to load cog: {e}")
                traceback.print_exc()
            
            await self.tree.sync()
            self.update_status.start()
            self.health_check.start()
            
        except Exception as e:
            logger.error(f"Setup hook error: {e}")
            raise

    async def on_ready(self):
        """When bot connects to Discord"""
        global bot_name
        bot_name = str(self.user)
        
        logger.info(f"\n🔗 Connected as {bot_name}")
        logger.info(f"🌐 Serving {len(self.guilds)} servers")
        
        # Start Flask if running on Render
        if os.environ.get('RENDER') or os.environ.get('PORT'):
            try:
                flask_thread = threading.Thread(target=run_flask, daemon=True)
                flask_thread.start()
                logger.info("🚀 Flask server started in background for Render")
            except Exception as e:
                logger.error(f"Failed to start Flask: {e}")

    @tasks.loop(minutes=5)
    async def update_status(self):
        """Update bot presence periodically"""
        try:
            if self._shutdown:
                return
                
            activity = discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{len(self.guilds)} servers"
            )
            await self.change_presence(activity=activity)
        except Exception as e:
            logger.warning(f"⚠️ Status update failed: {e}")

    @tasks.loop(minutes=10)
    async def health_check(self):
        """Periodic health check and cleanup"""
        try:
            if self._shutdown:
                return
                
            # Log uptime and memory usage
            uptime = time.time() - self.start_time
            logger.info(f"Bot uptime: {uptime:.0f}s, Guilds: {len(self.guilds)}")
            
            # Force garbage collection
            import gc
            gc.collect()
            
        except Exception as e:
            logger.error(f"Health check error: {e}")

    @update_status.before_loop
    async def before_status_update(self):
        await self.wait_until_ready()

    @health_check.before_loop
    async def before_health_check(self):
        await self.wait_until_ready()

    async def on_error(self, event_method: str, *args, **kwargs):
        """Global error handler"""
        logger.error(f"Error in {event_method}: {traceback.format_exc()}")

    async def close(self):
        """Cleanup on shutdown"""
        logger.info("Shutting down bot...")
        self._shutdown = True
        
        # Stop background tasks
        self.update_status.cancel()
        self.health_check.cancel()
        
        # Close session
        if self.session:
            await self.session.close()
        
        await super().close()

def signal_handler(signum, frame):
    """Handle shutdown signals gracefully"""
    logger.info(f"Received signal {signum}, shutting down...")
    sys.exit(0)

async def main():
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    bot = Bot()
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt")
        await bot.close()
    except Exception as e:
        logger.error(f"⚠️ Critical error: {e}")
        traceback.print_exc()
        await bot.close()
    finally:
        # Ensure cleanup
        if not bot.is_closed():
            await bot.close()

if __name__ == "__main__":
    # Special handling for Render's environment
    if os.environ.get('RENDER') or os.environ.get('PORT'):
        asyncio.run(main())
    else:
        bot = Bot()
        bot.run(TOKEN)