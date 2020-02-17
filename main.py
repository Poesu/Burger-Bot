import asyncio
from makeburger import make_burger
from discord.ext.commands import Bot
import config

TOKEN = config.token

client = Bot(command_prefix='>>')


@client.command()
async def burger(ctx):
	burger = make_burger()
	await ctx.channel.send(burger)

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed():
		print("Current servers:")
		for server in client.guilds:
			print(server.name)
		print('\n')
		await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)