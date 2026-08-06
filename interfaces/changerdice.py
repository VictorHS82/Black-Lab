from abc import ABC, abstractmethod

class ChangerDice(ABC):
    """
    Classe abstrata para definir a interface de mudança de dados.
    Utilizar em jogos que usem dados não numericos.
    Ex: Assimilação RPG.
    """
    @abstractmethod
    async def changer_manager(self, asi_message: str) -> str:
        pass

    @abstractmethod
    async def verify(self, cut_message: str) -> bool:
        pass

    @abstractmethod
    async def change(self, dados: dict) -> str:
        pass