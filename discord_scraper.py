import discord
from discord.ext import commands
import os  # Import the os module for file manipulation

# Initialize the intents object and set message_content to True
intents = discord.Intents.default()
intents.message_content = True

# Prompting the user for server name and bot token
server_name = input("Enter the name of the Discord server: ")
bot_token = input("Enter your bot token: ")

bot = commands.Bot(command_prefix=",", intents=intents)


async def download_messages(channel, filename):
    all_messages = []
    try:
        async for message in channel.history(limit=None, oldest_first=True):
            if (
                message.content.strip()
            ):  # This will be False for empty or whitespace-only strings
                all_messages.append(f"{message.author}: {message.content}")

        # Saving to a text file
        with open(filename, "w", encoding="utf-8") as f:
            for msg in all_messages:
                f.write(f"{msg}\n")

        print(f"Messages from #{channel.name} have been saved to '{filename}'")
    except Exception as e:
        print(f"Could not access #{channel.name} due to: {str(e)}")


async def download_forum_messages(channel, filename):
    all_messages = []
    all_threads = channel.threads
    for thread in all_threads:
        try:
            async for message in thread.history(limit=None, oldest_first=True):
                if message.content.strip():  # Skip empty or whitespace-only strings
                    all_messages.append(f"{message.author}: {message.content}")

            # Save to file
            with open(filename, "w", encoding="utf-8") as f:
                for msg in all_messages:
                    f.write(f"{msg}\n")

            print(f"Messages from #{thread.name} have been saved to '{filename}'")
        except Exception as e:
            print(f"Could not access #{thread.name} due to: {str(e)}")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    guild = discord.utils.get(bot.guilds, name=server_name)

    if guild:
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                filename = f"{channel.name}_messages.txt"
                if os.path.exists(filename):
                    print(f"Skipping #{channel.name} as '{filename}' already exists.")
                    continue
                await download_messages(channel, filename)
            elif isinstance(channel, discord.Thread):
                filename = f"{channel.parent.name}_{channel.name}_thread_messages.txt"
                if os.path.exists(filename):
                    print(
                        f"Skipping thread {channel.name} in #{channel.parent.name} as '{filename}' already exists."
                    )
                    continue
                await download_messages(channel, filename)
            elif str(channel.type) == "forum":
                filename = f"{channel.name}_forum_messages.txt"
                if os.path.exists(filename):
                    print(
                        f"Skipping forum #{channel.name} as '{filename}' already exists."
                    )
                    continue
                await download_forum_messages(channel, filename)


bot.run(bot_token)
