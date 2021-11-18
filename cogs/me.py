import discord
from discord.ext import commands

from tools import *

class me(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def me(self, ctx, *, do):
        embed = discord.Embed(
            description=f"{ctx.author.mention} делает {do}"
        )

def setup(client: discord.Client):
    client.add_cog(me(client))
