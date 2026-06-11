import discord
import os
from discord.ext import commands
from cogs.utilidades import setup
from dotenv import load_dotenv
class Soul(commands.Bot):
    def __init__(self):
        intents=discord.Intents.all()
        super().__init__(command_prefix="!",
                         intents=intents
        )

    async def setup_hook(self):
         for arquivo in os.listdir("./cogs"):
            if arquivo.endswith(".py"):
                await self.load_extension(
                    f"cogs.{arquivo[:-3]}"
                )
    
    async def on_ready(self):
        print(f'Bot {self.user} logado')        

load_dotenv()
token: str | None = os.getenv("TOKEN_RUN_BOT")
if token is None:
    raise ValueError("Cadê o token?")

bot = Soul()

@bot.tree.command(name="ping", description="Responde com Saí fora!")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message("Saí fora!")

bot.run(token)