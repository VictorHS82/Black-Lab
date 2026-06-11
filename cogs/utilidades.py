from discord.ext import commands
# comandos.py
class Utilidades(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Saí fora!")

async def setup(bot):
    await bot.add_cog(Utilidades(bot))