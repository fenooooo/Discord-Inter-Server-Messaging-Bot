
# Discord Inter-Server Messaging Bot

This bot allows users to send messages across linked channels on different Discord servers. The bot ensures that messages sent from a designated channel will appear on other servers with the linked channels.

## Features

- Sends messages across multiple servers in specified channels
- Simple command-based usage

## Setup

1. Clone the repository.
2. Install dependencies:

   ```
   pip install discord.py python-dotenv
   ```

3. Create a `.env` file and add your API keys and Discord bot token:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   COMMAND_PREFIX=!
   CHANNEL_IDS=123456789012345678,987654321098765432  # Add your channel IDs here
   ```

4. Run the bot:

   ```
   python bot.py
   ```

## Commands

- `!sendmsg <message>`: Sends a message from one linked channel to all other linked channels across different servers.

## Requirements

- Python 3.6 or higher
- discord.py
- python-dotenv

## Notes

- Make sure to add the bot to all servers where you want the inter-server messaging to occur.
- The bot will only send messages from and to the channels listed in the `CHANNEL_IDS` environment variable.
