from discord.ext import commands
import discord

from utils import mods_or_owner


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog Загружен успешно\n-----")


    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason: str = "Вы плохо себя вели и были кикнуты"):
        if member is not None:
            await ctx.guild.kick(member, reason=reason)
        else:
            await ctx.send("Укажите пользователя, которого нужно исключить, упоминая и причину")

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "Выплохо себя вели и были забанены"):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
        else:
            await ctx.send("Укажите пользователя, которого нужно исключить, упоминая")

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: str = "", reason: str = "Вас разблокировали. Время вышло. Пожалуйста, веди себя хорошо"):
        if member == "":
            await ctx.send("Укажите пользователя, которого нужно исключить, упоминая и причину")
            return

        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                await ctx.send("Пользователь разблокирован!")
                return
        await ctx.send("Пользователь не найден в заблокированном списке.")


def setup(bot):
    bot.add_cog(Moderator(bot))
