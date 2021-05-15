import os

from mongoengine import *

from discord.ext import commands

from settings import *

connect('discord', host='mongodb+srv://luhhtuuk:Froog2020d@cluster0.eavxh.mongodb.net/testdata?retryWrites=true&w=majority', username='luhhtuuk',
        password='Froog2020d', authentication_source="testdata")

bot = commands.Bot(command_prefix="a!")

for filename in os.listdir('cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('ODQzMDMwNTI1MjQ0NDczMzQ0.YJ97Ww.s1AQuZfI98BDBXxRg0eXJgRV1SE')