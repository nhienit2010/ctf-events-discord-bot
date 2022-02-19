from sys import prefix
from config import *
from lib import *
import discord
import aiocron

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is working!!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == ".hello":
        await message.channel.send("Hello my friend")
    
    if message.content == ".help":
        msg = "Help: \n\n"
        msg += ".help : list all bot commands"
        msg += ".hello : Say hello to bot\n"
        msg += ".events : get 3 ctf-events upcoming\n"
    
    if message.content == ".events":
        events = getEvents()
        for event in events:
            await message.channel.send("```" + event + "```")

@aiocron.crontab('0 0 * * 5')
async def cornjob1():
    channel = client.get_channel(CTF_EVENTS_CHANNEL_ID)
    await channel.send("> CTF Events upcomming")
    events = getEvents()
    await channel.send("```" + '\n\n\n'.join(events) + "```")
    await channel.send("@everyone")

if __name__ == "__main__":
    client.run(BOT_TOKEN)