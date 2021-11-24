# Soon i make it cog.
import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
	print("Started")

@client.command()
async def cleanup(ctx):
	await ctx.channel.purge(limit=999)
	embed = discord.Embed(
	title = "Очищено ✅",
	color = discord.Color.green()
	)
	await ctx.send(embed=embed, delete_after = 5)

@client.command()
async def lock(ctx):
	embed = discord.Embed(
	title = "Channel closed by operator",
	description = f"This channel closed by {ctx.author.mention} and nobody except operators of this server cant write in this channel.",
	color = discord.Color.green(),
	timestamp = datetime.datetime.now()
	)
	await ctx.message.delete()
	await ctx.send(embed=embed)
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)

client.run("OTEwOTIzMTA4NjE2MTE4Mjcy.YZZ5QQ.SjzOTnAsOsoV86jhBWPF6lFPZv0")
