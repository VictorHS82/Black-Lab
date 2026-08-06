import re

from game_logic.diceman import Diceman


class Assimilador:
    def __init__(self, bot):
        self.bot = bot
        self.diceman = Diceman(bot)
        self.assimilitaded_dice = {
            "d6": {
                "1": "",
                "2": "",
                "3": "pressão",
                "4": "pressão",
                "5": ["Adaptação", "pressão"],
                "6": "Sucesso",
            },
            "d10": {
                "1": "",
                "2": "",
                "3": "pressão",
                "4": "pressão",
                "5": ["Adaptação", "pressão"],
                "6": "Sucesso",
                "7": ["Sucesso", "Sucesso"],
                "8": ["Sucesso", "Adaptação"],
                "9": ["Sucesso", "Adaptação", "Pressão"],
                "10": ["Sucesso", "Sucesso", "Pressão"],
            },
            "d12": {
                "1": "",
                "2": "",
                "3": "pressão",
                "4": "pressão",
                "5": ["Adaptação", "pressão"],
                "6": "Sucesso",
                "7": ["Sucesso", "Sucesso"],
                "8": ["Sucesso", "Adaptação"],
                "9": ["Sucesso", "Adaptação", "Pressão"],
                "10": ["Sucesso", "Sucesso", "Pressão"],
                "11": ["Sucesso", "Adaptação", "Adaptação", "Pressão"],
                "12": ["Pressão", "Pressão"],
            },
        }

    async def genesteal(self, asi_message: str):
        infected = await self.infect(asi_message)
        if not infected:
            return "O dado não é assimilável."

        dados = await self.diceman.roll_dice_details(asi_message)
        return await self.transform(dados)

    async def infect(self, cut_message: str):
        parasite = r"^(?:\d*d(?:6|10|12))(?:\+(?:\d*d(?:6|10|12)))*$"
        return bool(re.fullmatch(parasite, cut_message))

    async def transform(self, dados):
        linhas = []

        for bloco in dados.get("blocos", []):
            if bloco.get("kind") != "dice":
                continue

            label = f"d{bloco['lados']}"
            tabela = self.assimilitaded_dice.get(label)
            if not tabela:
                continue

            for valor in bloco.get("resultados", []):
                resultado = tabela.get(str(valor), "")
                if isinstance(resultado, list):
                    display = ", ".join(resultado)
                else:
                    display = resultado

                linhas.append(f"{label}: [{display}]")

        return "\n".join(linhas)
