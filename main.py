import discord
from discord import Intents
import os
import asyncio
from datetime import datetime
from alarm_data import get_alarm_data

TOKEN = 'YOUR_BOT_TOKEN'
CHANNEL_ID = 1234567890

intents = Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

async def check_alarm():
    while True:
        alarm_data = get_alarm_data()

        if alarm_data:
            city = alarm_data['city']
            time = datetime.fromtimestamp(alarm_data['time'])
            duration = alarm_data['duration']

            msg = f"ALARM: {city} | Time: {time} | Duration: {duration} seconds"
            channel = client.get_channel(CHANNEL_ID)
            await channel.send(msg)

        await asyncio.sleep(60)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await check_alarm()

client.run(TOKEN)
