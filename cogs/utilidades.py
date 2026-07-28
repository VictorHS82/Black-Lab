from discord.ext import commands

class Utilidades(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="ping", description="Responde com Saí fora!")
    async def ping(self, ctx):
        await ctx.reply("Saí fora!")

async def setup(bot):
    await bot.add_cog(Utilidades(bot))