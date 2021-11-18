import os

name = input("Название команды: ")

template = """import disocrd
from discord.ext import commands

from tools import *

class %name%(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def %name%(self, ctx):
        pass

def setup(client: discord.Client):
    client.add_cog(%name%(client))
""".replace("%name%", name)

with open("../cogs/" + name + ".py", "w") as w:
    w.write(template)

print("Готово")