from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog Загружен успешно\n-----")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test done!")


def setup(bot):
    bot.add_cog(Test(bot))
