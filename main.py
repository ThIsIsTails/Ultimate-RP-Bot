# encode=UTF-8

import discord
from discord.ext.commands import Bot
from logfox import logger
import atexit
import os

client = Bot(command_prefix="!", intents=discord.Intents.all())
log = logger.logger("logs/", True)
token = "OTEwOTIzMTA4NjE2MTE4Mjcy.YZZ5QQ.EYYGEhwJdorGQCVzlIWSQDjIaQ8"

def exit_handler():
    log.warn('Exiting...')

atexit.register(exit_handler)

@client.event
async def on_ready():
    log.info("There sessions starts...")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        try:
            client.load_extension(f"cogs.{file[:-3]}")
            log.info(f"Loaded {file}.")
        except Exception as error:
            log.exception(f"Exception on {file}: {error}")

client.run(token)