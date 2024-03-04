# %%

class ft_tqdm():
    def __init__(self, x: object):
        self.internal_iterator = iter(x)
        self.current = 0
        self.max = len(x)

    def __iter__(self):
        return self

    def __next__(self):
        perProgress = self.current / self.max
        perProgressRemain = 1 - perProgress
        consoleWidth = 166

        print(f"\r{int(100 * perProgress)}%|{int(perProgress * consoleWidth) * "█"}"
              + f"{int(perProgressRemain * consoleWidth) * " "}|" +
              f" {self.current}/{self.max}", end="")
        self.current += 1
        return next(self.internal_iterator)
