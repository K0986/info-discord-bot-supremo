#!/usr/bin/env python3
"""
Health check script for the Discord bot
This can be used to monitor if the bot is running properly
"""

import requests
import sys
import os
from datetime import datetime

def check_bot_health():
    """Check if the bot is responding to health checks"""
    try:
        # Get the bot URL from environment or use default
        bot_url = os.environ.get('BOT_URL', 'http://localhost:10000')
        
        # Check health endpoint
        response = requests.get(f"{bot_url}/health", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Bot is healthy: {data}")
            return True
        else:
            print(f"❌ Bot health check failed: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to bot: {e}")
        return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

if __name__ == "__main__":
    print(f"🔍 Checking bot health at {datetime.now()}")
    success = check_bot_health()
    sys.exit(0 if success else 1)
