# bot.py
import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
TARGET = os.getenv('TARGET')
REYNE = os.getenv('REYNE')

print(TOKEN)

client = discord.Client()
insults = [
    "You couldnt be further from the point mate.",
    "What a stupid opinion.",
    "Please. Just stop.",
    "Fucking hell, will you ever quit talking shit?",
    "I dont even know why i read your messages any more.",
    "Out of all the dumb things you say, this one takes the cake.",
    "You just out-do yourself every time dont you?",
    "Shut the fuck up. Like seriously. Just shut the fuck up.",
    "You have as much talent as a giraffe in dark glasses trying to get into a polar-bears-only club."
    "Dont use long words to make yourself sound smart, buddy.",
    "I dont think ive ever heard anything dumber than that to be honest.",
    "You are a sad strange little man, and you have my pity.",
    "Look at this guy :joy:",
    "Do you even read your messages before you send them?",
    "No wonder your parents tell their friends you're dead.",
    "Shut up you fucking paramecium.",
    "Ohhhhh myyyyy god shutttt up.",
    "Im a bot without emotions, but reading that made me angry as fuck.",
    "Listen to this virgin LMAO.",
    "Alright, sit down kiddo, you've made yourself look dumb enough.",
    "Evidently, you have the intellectual capacity that would have a tough time challenging a fucking pool noodle.",
    "Keep that shit up and ill delete the whole fucking server.",
    "You're seriously as sharp as a spoon hey?"
]

def getMessage():
    return random.choice(insults)

@client.event
async def on_ready():
    server = findServer()
    print(f'{client.user} has connected to: {server.name}')

def findServer():
    for guild in client.guilds:
        if guild.name == SERVER:
            return guild

@client.event
async def on_message(message):
    #if its the bot
    if str(message.author) == client.user:
        return
    
    #if its the target
    if str(message.author) == TARGET:
        if rollMessage(10):          
            print('Message:')
            print(f'{message.author} - {message.content}')
            await message.channel.send(getMessage())

    #if its reyne being a retard
    if str(message.author) == REYNE:
        if message.content.find("@boys") == 0 or message.content.find("@Boys") == 0:
            await message.delete()

    #if its anyone else
    else:
        if rollMessage(20):
            if rollMessage(5):
                changeTarget(TARGET, message.author, message)
            else:            
                print('Message:')
                print(f'{message.author} - {message.content}')
                await message.channel.send(getMessage())

def rollMessage(chance):
    if random.randint(0, chance) == chance:
        return True
    else:
        return False

def changeTarget(oldTarget, newTarget, message):
    message.channel.send("Nope thats fucking it, ive had enough")
    message.channel.sennd(f'@{str(oldTarget)} - Im done with you. Your turn @{str(newTarget)}')
    TARGET = str(newTarget)

client.run(TOKEN)