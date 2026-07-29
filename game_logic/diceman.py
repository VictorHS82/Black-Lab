from discord.ext import commands
import random
import re


class Diceman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def breaking_it_down(self, message: str):
        message = message.strip()
        if not message:
            return []

        partes = re.findall(r"[+-]?\s*[^+-]+", message)
        return [parte.strip() for parte in partes if parte.strip()]

    async def roll_dice(self, message: str):
        grupos = await self.breaking_it_down(message)
        if not grupos:
            return "Nenhum dado para rolar."

        blocos = []
        total = 0

        for grupo in grupos:
            parsed = await self.parse_dice(grupo)
            if not parsed:
                continue

            if parsed["kind"] == "dice":
                resultados = []
                for _ in range(parsed["quantidade"]):
                    resultados.append(random.randint(1, parsed["lados"]))

                valor = sum(resultados) * parsed["sinal"]
                blocos.append({
                    "kind": "dice",
                    "resultados": resultados,
                    "quantidade": parsed["quantidade"],
                    "lados": parsed["lados"],
                    "valor": valor,
                })
                total += valor
            else:
                valor = parsed["valor"] * parsed["sinal"]
                blocos.append({
                    "kind": "modifier",
                    "valor": valor,
                })
                total += valor

        if not blocos:
            return "Nenhum dado para rolar."

        partes_texto = []
        for index, bloco in enumerate(blocos):
            if bloco["kind"] == "dice":
                texto = f"[{', '.join(str(v) for v in bloco['resultados'])}] {bloco['quantidade']}d{bloco['lados']}"
            else:
                valor = bloco["valor"]
                texto = str(valor)

            if index == 0:
                partes_texto.append(texto)
            else:
                if bloco["kind"] == "modifier":
                    sinal = "+" if bloco["valor"] >= 0 else "-"
                    partes_texto.append(f"{sinal} {abs(bloco['valor'])}")
                else:
                    sinal = "+" if bloco["valor"] >= 0 else "-"
                    partes_texto.append(f"{sinal} {texto}")

        return f"{' '.join(partes_texto)} = {total}"

    async def parse_dice(self, token: str):
        token = token.strip()
        if not token:
            return None

        sinal = 1
        if token.startswith("-"):
            sinal = -1
            token = token[1:]
        elif token.startswith("+"):
            token = token[1:]

        token = token.strip()
        if not token:
            return None

        if "d" not in token:
            return {
                "kind": "modifier",
                "sinal": sinal,
                "valor": int(token),
            }

        quantidade_str, lados_str = token.split("d", 1)
        quantidade = 1 if quantidade_str == "" else int(quantidade_str)
        lados = int(lados_str)

        return {
            "kind": "dice",
            "sinal": sinal,
            "quantidade": quantidade,
            "lados": lados,
        }
