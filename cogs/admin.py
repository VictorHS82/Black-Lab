from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, cog):

        try:
            await self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f" Cog '{cog}' carregado.")
        except Exception as e:
            await ctx.send(f" Erro ao carregr '{cog}':\n{e}")
    
    @commands.command()
    async def reload(self, ctx, cog):

        try:
            await self.bot.reload_extension(f"cogs.{cog}")
            await ctx.send(f" Cog '{cog}' recarregado.")
        except Exception as e:
            await ctx.send(f" Erro ao recarregar '{cog}':\n{e}")
    
    @commands.command()
    async def unload(self, ctx, cog):

        try:
            await self.bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"cog '{cog}' desabilitado.")
        except Exception as e:
            await ctx.send(f"Erro ao desabilitar '{cog}':\n{e}")


async def setup(bot):
    await bot.add_cog(Admin(bot))