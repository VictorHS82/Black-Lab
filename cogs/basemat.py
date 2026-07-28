from discord.ext import commands

class Basemat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="soma", description="Responde com o resultado de uma soma")
    async def soma(self, ctx):
        await ctx.reply("Em construção")

async def setup(bot):
    await bot.add_cog(Basemat(bot))