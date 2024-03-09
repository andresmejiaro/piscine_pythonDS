# %%
from abc import ABC, abstractmethod


class Character(ABC):
    """Any character describing their status"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor takes name and is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def abstract(self):
        "does nothing just to make abstract"
        pass

    def die(self):
        "He dead"
        self.is_alive = False


class Stark(Character):
    """ Best Wolves in Westeros"""

    def abstract(self):
        pass


# # %%
# Ned = Stark("Ned")
# # %%
# print(Ned.__dict__)
# print(Ned.is_alive)
# Ned.die()
# print(Ned.is_alive)
# print(Ned.__doc__)
# print(Ned.__init__.__doc__)
# print(Ned.die.__doc__)
# print("---")
# Lyanna = Stark("Lyanna", False)
# print(Lyanna.__dict__)
# # %%
# hodor = Character("hodor")
