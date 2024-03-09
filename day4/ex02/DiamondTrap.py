# %%
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    "A Monster I tell you"

    def __init__(self, first_name: str, is_alive: bool = True):
        "He has daddy's eyes and hair"
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        "look at me"
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        "feel my belly"
        self.hairs = hairs

    def get_eyes(self):
        "hex"
        return self.eyes

    def get_hairs(self):
        "b"
        return self.hairs

# #%%
# Joffrey = King("Joffrey")
# print(Joffrey.__dict__)
# Joffrey.set_eyes("blue")
# Joffrey.set_hairs("light")
# print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print(Joffrey.__dict__)
