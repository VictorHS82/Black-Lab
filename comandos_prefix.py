# comandos.py
def setup(bot):
    @bot.command(name="ping")
    async def olamundo(ctx):
        await ctx.send("Saí fora!")