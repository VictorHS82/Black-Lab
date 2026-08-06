from discord.ext import commands
from game_logic.assimilador import Assimilador
from game_logic.diceman import Diceman


class Basemat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.diceman = Diceman(bot)
        self.assimilador = Assimilador(bot)

    @commands.hybrid_command(name="roll", description="Role dados")
    async def roll(self, ctx, expressao: str):
        resposta = await self.diceman.roll_dice(expressao)
        await ctx.reply(resposta)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not message.content.startswith("!"):
            return

        comando = message.content[1:].strip()
        if not comando:
            return

        if comando.startswith("a"):
            expressao = comando[1:].strip()
            if not expressao:
                await message.reply("Uso: !a<dados>, por exemplo !ad6")
                return

            if not await self.assimilador.infect(expressao):
                await message.reply("O dado não é assimilável.")
                return

            resposta = await self.assimilador.genesteal(expressao)
            await message.reply(str(resposta))
            return

        resposta = await self.diceman.roll_dice(comando)
        await message.reply(resposta)


async def setup(bot):
    await bot.add_cog(Basemat(bot))