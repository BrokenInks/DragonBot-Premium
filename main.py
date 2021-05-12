import os

from mongoengine import *

from discord.ext import commands

from settings import *

connect('discord', host='localhost', username='root',
        password='root', authentication_source="admin")

bot = commands.Bot(command_prefix="d!")

for filename in os.listdir('cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('ODQxNzE1NjY3NzE1MzU4ODEx.YJqyzQ.UTkwdbShHqRm1I15UOfj7lhpkM0')
print('Client Online')
