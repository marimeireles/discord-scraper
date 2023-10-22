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
    
3. `pip install discord.py`
4. **Clone this repository** or download the script.

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
3. **Configure the Script**:
    - Open the Python script and replace `'Your Server Name'` with the name of your Discord server.
    - Replace `'general'` with the name of the channel from which you want to collect messages.
    - Replace `'YOUR_BOT_TOKEN'` with the token you copied earlier.

## Usage

1. Open your command prompt and navigate to the directory where the script is located.
2. Run the script:
    
    ```
    python discord_scraper.py
    ```
    
3. `python your_script_name.py`
4. The script will print all messages from the specified channel to the console. You can modify the script to save these messages to a file if needed.
