# %%
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    "they gave us this"
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    "Student info"
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id(),)

    def __post_init__(self):
        "generate the email after the init"
        self.login = self.name[0] + self.surname


# #%%
# student = Student(name = "Edward", surname = "agle")
# print(student)
# # %%
# student = Student(name = "Edward", surname = "agle", id = "toto")
# print(student)
# # %%
