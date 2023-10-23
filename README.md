# Discord Message Collector

A Python script that uses `discord.py` to collect all messages from a specified channel in a Discord server.

## Prerequisites

- Python 3.x
- `discord.py` library
- A Discord account and a server where you have administrative or read message permissions

## Installation

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).
2. **Install `discord.py`**: Open your command prompt and run:
    
    ```
    pip install discord.py
    ```
3. **Clone this repository** or download the script.

## Setup

1. **Create a Discord Bot**:
    - Go to [Discord Developer Portal](https://discord.com/developers/applications)
    - Click "New Application" and give it a name.
    - Navigate to the "Bot" tab and click "Add Bot".
    - Under the "TOKEN" section, click "Copy" to copy your bot token.
2. **Invite the Bot to Your Server**:
    - Go to the "OAuth2" tab in your bot's application page.
    - Under "OAuth2 URL Generator", select "bot" in the scopes section.
    - Choose the necessary permissions (at minimum, "Read Messages").
    - Copy the generated URL and use it to invite the bot to your server.
2. **Activate "Message Content Intent"**:
   - Go to the "Bot" session
   - Scroll down in the "Privileged Gateway Intents" area
   - Activate "Message Content Intent"

## Usage

1. Open your command prompt and navigate to the directory where the script is located.
2. Run the script:
    
    ```
    python discord_scraper.py
    ```
    
3. The script will prompt you to enter the name of the Discord server and the bot token.
    - For the server name, enter the name of the Discord server you want to collect messages from.
    - For the bot token, paste the token you copied earlier.
4. Check the Output
    - The script will save all messages from each text channel to a separate text file, named after the channel (e.g., `general_messages.txt`, `random_messages.txt`, etc.).
    - Messages that could not be accessed will be reported in the console.
