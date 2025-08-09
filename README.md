# Free Fire Info Bot

A Discord bot that provides detailed information about Free Fire players using their UID.

## Features

- 🎮 Get detailed player information by UID
- 📊 View player stats, clan info, and achievements
- 🖼️ Generate player outfit images
- ⚙️ Configurable channel restrictions
- 🛡️ Rate limiting and cooldown system
- 🌐 Optimized for Render deployment

## Commands

- `!info <UID>` - Get player information
- `!setinfochannel <#channel>` - Set allowed channel (Admin only)
- `!removeinfochannel <#channel>` - Remove channel restriction (Admin only)
- `!infochannels` - List allowed channels

## Deployment on Render

### Prerequisites

1. Create a Discord application and bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token
3. Create a Render account

### Setup

1. **Fork/Clone this repository**

2. **Set up on Render:**
   - Create a new Web Service
   - Connect your GitHub repository
   - Set environment variables:
     - `TOKEN`: Your Discord bot token
     - `PORT`: 10000 (or leave default)

3. **Deploy:**
   - Render will automatically build and deploy your bot
   - The bot will start automatically

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TOKEN` | Discord bot token | Yes |
| `PORT` | Port for web server | No (default: 10000) |
| `RENDER` | Set by Render automatically | No |

## Troubleshooting

### Bot Keeps Disconnecting

**Common Causes:**
1. **Memory leaks** - Fixed in latest version
2. **Resource limits** - Render free tier has strict limits
3. **Network timeouts** - Added timeout handling
4. **File system issues** - Disabled file operations on Render

**Solutions:**
- ✅ Use the latest code with improved resource management
- ✅ Monitor logs in Render dashboard
- ✅ Check bot status at `/health` endpoint

### Performance Issues

**Optimizations Made:**
- Single `aiohttp.ClientSession` for all requests
- Proper resource cleanup
- Garbage collection after operations
- Timeout handling for all requests
- Disabled file operations on Render

### Monitoring

**Health Check:**
```bash
curl https://your-bot-name.onrender.com/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "bot": "YourBotName#1234"
}
```

### Logs

Check Render logs for:
- Connection errors
- Memory usage
- API timeouts
- Resource cleanup

## Development

### Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export TOKEN=your_discord_bot_token
```

3. Run the bot:
```bash
python app.py
```

### File Structure

```
├── app.py              # Main bot file
├── cogs/
│   └── infoCommands.py # Bot commands
├── requirements.txt     # Dependencies
├── render.yaml         # Render configuration
├── Procfile           # Process file
└── README.md          # This file
```

## Technical Details

### Architecture

- **Discord.py**: Bot framework
- **Flask**: Web server for health checks
- **Waitress**: Production WSGI server
- **aiohttp**: Async HTTP client
- **Render**: Hosting platform

### Resource Management

- Single HTTP session per bot instance
- Automatic garbage collection
- Proper cleanup on shutdown
- Timeout handling for all requests
- Memory-efficient operations

### Security

- Environment variable for sensitive data
- Input validation for UIDs
- Rate limiting per user
- Channel permission checks

## Support

If you encounter issues:

1. Check the Render logs
2. Verify your bot token is correct
3. Ensure the bot has proper permissions
4. Test the health endpoint

## License

This project is developed by THUG.

---

**Note:** This bot is optimized for Render's free tier limitations. For production use, consider upgrading to a paid plan or using a different hosting provider.

