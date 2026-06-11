import discord
from discord.ext import commands
from comandos_prefix import setup

class Soul(commands.Bot):
    def __init__(self):
        intents=discord.Intents.all()
        super().__init__(command_prefix="!",
                         intents=intents
        )

    async def on_ready(self):
        print(f'Bot {self.user} logado')        

bot = Soul()

setup(bot)

@bot.tree.command(name="ping", description="Responde com Saí fora!")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message("Saí fora!")

# @bot.command(name="ping")
# async def olamundo(ctx):
#     await ctx.send("Saí fora!")

bot.run()