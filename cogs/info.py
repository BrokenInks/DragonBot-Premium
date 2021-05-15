from discord.ext import commands
import discord

import datetime

from settings import MODERATOR_ROLE_NAME


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog Загружен успешно\n-----")

    @commands.command(brief="Creates an invite link to the channel")
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)


def setup(bot):
    bot.add_cog(Info(bot))
