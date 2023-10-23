import discord
from discord.ext import commands

# Prompting the user for server name and bot token
server_name = input("Enter the name of the Discord server: ")
bot_token = input("Enter your bot token: ")

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = discord.utils.get(bot.guilds, name=server_name)

    if guild:
        for channel in guild.text_channels:
            all_messages = []
            try:
                async for message in channel.history(limit=None, oldest_first=True):
                    all_messages.append(f"{message.author}: {message.content}")

                # Saving to a text file
                with open(f'{channel.name}_messages.txt', 'w', encoding='utf-8') as f:
                    for msg in all_messages:
                        f.write(f"{msg}\n")

                print(f"Messages from #{channel.name} have been saved to '{channel.name}_messages.txt'")
            except Exception as e:
                print(f"Could not access #{channel.name} due to: {str(e)}")

bot.run(bot_token)

