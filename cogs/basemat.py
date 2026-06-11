from discord.ext import commands

class Basemat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def soma(self,ctx):
        await ctx.send("blood")

async def setup(bot):
    await bot.add_cog(Basemat(bot))