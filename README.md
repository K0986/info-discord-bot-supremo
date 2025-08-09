# Free Fire info Discord Bot

![Status](https://img.shields.io/badge/status-active-brightgreen)

An asynchronous Discord bot that provides a **REST API** to retrieve detailed information about a **Free Fire account** using its UID.  
It returns profile data such as level, rank, guild info, credit score, social preferences, and more. The bot includes a built-in Flask server for uptime support on Render.

## 🚀 Features

- Integrated API to fetch Free Fire account data via UID
- Detailed data: level, rank, guild, credit score, full profile
- Secure credentials using `.env`
- Built-in Flask server for Render deployment

## Requirements

- Python 3.8+
- A Discord bot token
- A `.env` file containing:
  ```ini
  TOKEN=your_bot_token
  PORT=10000
  ```

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/K0986/info-discord-bot-supremo
   cd info-discord-bot-supremo
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your credentials:
   ```ini
   TOKEN=your_bot_token
   PORT=10000
   ```
5. Run the bot:
   ```sh
   python app.py
   ```

## 🚀 Render Deployment

This bot is optimized for deployment on Render. Follow these steps:

1. **Fork or clone** this repository to your GitHub account
2. **Go to [Render.com](https://render.com)** and sign up/login
3. **Create a new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select your repository
   - Choose "Python" as the environment
4. **Configure the service:**
   - **Name:** `freefire-info-bot` (or any name you prefer)
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
5. **Add Environment Variables:**
   - `TOKEN`: Your Discord bot token
   - `PORT`: `10000` (Render will set this automatically)
6. **Deploy!** Render will automatically build and deploy your bot

## 📸 Demo


<div align="center">


<img width="591" height="820" alt="image" src="https://github.com/user-attachments/assets/9d07608d-e6d2-4afd-9a1f-ba16aeeca59f" />
<img width="538" height="377" alt="image" src="https://github.com/user-attachments/assets/f748a4c6-7670-45e4-ac08-5fd8fc746ab9" />
 
</div>



## Usage

- Use `!info <user_id>` in a Discord server where the bot is present.
- The bot will fetch  information from [free-fire-info-api](https://github.com/paulafredo/free-fire-info-api) and respond with an embedded message.



## 🛠️ Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"**, and give your bot a name.
3. In the left sidebar, go to the **"Bot"** section and click **"Add Bot"**, then confirm with **"Yes, do it!"**.
4. Under the **Token** section, click **"Reset Token"** or **"Copy"** to get your `TOKEN`.
5. Go to **"General Information"** and copy the `APPLICATION_ID`.
6. Paste both values into your `.env` file:
      ```ini
   TOKEN=your_bot_token
   ```


## 🔗 Invite the Bot to a Discord Server

1. Go to **OAuth2 > URL Generator** in the Developer Portal.
2. Under **Scopes**, check:
   - `bot`
   - `applications.commands`
3. Under **Bot Permissions**, check at least:
   - `Send Messages`
   - `Embed Links`
4. Copy the generated URL and open it in your browser to invite the bot to your server.


## 📚 Bot Commands

### `!info <user_id>`
Check whether a Free Fire account is **banned** or **not**.

- 📥 **Input:** a user ID (UID)





## Technologies Used

- Python
- Discord.py
- Flask
- dotenv

## License

This project is licensed under the MIT License. Feel free to use and modify it.

## Author

[Paul Alfredo](https://github.com/paulafredo)

