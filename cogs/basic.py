from discord.ext import commands
import discord

from utils import text_to_owo, notify_user


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog Загружен успешно\n-----")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Пожалуйста введите d!help для просмотра команд или же возможно эта команда для администратора либо создателя бота.")

    @commands.command(brief="Any message to owo")
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")


def setup(bot):
    bot.add_cog(Basic(bot))
