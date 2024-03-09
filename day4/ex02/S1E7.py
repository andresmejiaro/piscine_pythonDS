from S1E9 import Character


class Baratheon(Character):
    "Right of arms, rowers of westeros"

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor takes name and is_alive, all Baratheons are brown
        eyed and dark haired"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        "Heraldry Representation"
        tr = f"{self.first_name} {self.family_name}, "
        tr = tr + f"{self.eyes} eyed, {self.hairs} haired has "
        w = "yet to meet" if self.is_alive else "met"
        tr = tr + f"{w} their maker"
        return tr

    def __repr__(self) -> str:
        "Boring representation"
        tr = f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"
        return tr

    def abstract(self):
        "I'm a real class now"
        pass


class Lannister(Character):
    """They are broke"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor takes name and is_alive, all Lannister are blue
        eyed and light haired"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        "Westeros Poetry"
        tr = f"{self.first_name} {self.family_name}, "
        tr = tr + f"{self.eyes} eyed, {self.hairs} haired has "
        w = "yet to meet" if self.is_alive else "met"
        tr = tr + f"{w} their maker"
        return tr

    def __repr__(self) -> str:
        "Boring representation"
        tr = f"Vector: ('{self.family_name}','{self.eyes}','{self.hairs}')"
        return tr

    def create_lannister(*args, **kwargs):
        "Bastard king making machine in the making"
        to_return = Lannister(*args, **kwargs)
        return to_return

    def abstract(self):
        "I'm a real class now"
        pass

# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# # %%
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# Jaine = Lannister.create_lannister("Jaine", True)
# print(f"Name : {Jaine.first_name, type(Jaine).__name__},
    # Alive : {Jaine.is_alive}")
