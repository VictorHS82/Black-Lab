from discord.ext import commands
import random

class Basemat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="d", description="Responde com o resultado")
    async def d(self, ctx, lados: int):
        resultado = random.randint(1, lados)
        await ctx.reply(f"d{lados}: {resultado}") 

    @commands.Cog.listener()
    async def on_message(self, message):
        dados = []
        total = 0
        positive = True
        if message.author.bot:
            return

        if message.content.startswith("!"):
            comando = message.content[1:]
            if "+" in comando:
                dice, bonus = comando.split("+")
                quantidade, lados = dice.split("d")
            elif "-" in comando:
                dice, bonus = comando.split("-")
                quantidade, lados = dice.split("d")
                positive = False
            else:
                quantidade, lados = comando.split("d")
                bonus = 0
            if quantidade == "":
                quantidade = 1

            lados = int(lados)
            quantidade = int(quantidade)
            bonus = int(bonus)
            if positive == False:
                bonus = bonus*(-1)

            for i in range(quantidade):
                resultado = random.randint(1, lados)
                dados.append(resultado)
                total += resultado
            if bonus > 0:
                await message.reply(f"{quantidade}d{lados}+{bonus}: {dados}+{bonus} = {total+bonus}") 
            elif bonus == 0: 
                await message.reply(f"{quantidade}d{lados}: {dados} = {total}")
            elif bonus < 0:
                await message.reply(f"{quantidade}d{lados}{bonus}: {dados}{bonus} = {total+bonus}")
async def setup(bot):
    await bot.add_cog(Basemat(bot))