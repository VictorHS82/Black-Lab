import discord
import os
import re
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN_RUN_BOT")
if token is None:
    raise ValueError("Cadê o token?")

guild_id = os.getenv("GUILD_ID")
if guild_id is None:
    raise ValueError("Cadê o GUILD_ID?")
GUILD_ID = int(guild_id)

class Soul(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=["#","!"], intents=intents)
        self.local_guild = discord.Object(id=GUILD_ID)
        self._dice_pattern = re.compile(
            r"^(?:[+-]?(?:\d+)?d\d+(?:[+-]\d+)?)$"
        )

    async def setup_hook(self):
        print("Tentando carregar cogs de", os.getcwd())
        for arquivo in os.listdir("./cogs"):
            if arquivo.endswith(".py"):
                print("Carregando", arquivo)
                await self.load_extension(f"cogs.{arquivo[:-3]}")

        await self.tree.sync(guild=self.local_guild)
        await self.tree.sync()

    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.strip()
        if content.startswith("!"):
            comando = content[1:].strip()
            if self._dice_pattern.match(comando):
                return

        await self.process_commands(message)

    async def on_ready(self):
        print(f'Bot {self.user} logado')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

bot = Soul()

bot.run(token)