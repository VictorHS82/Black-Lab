import os

class TableManager():
    """
    Classe para sortear itens, eventos e etc de uma tabela prédefinida.
    """
    def __init__(self, table_name: str, table_path: str):
        self.table_name = table_name
        self.table_path = table_path

    async def get_table(self):
        pass

    async def roll_on_table(self):
        pass

    