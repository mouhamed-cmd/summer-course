# problem 1
class Soldier:
    """Represents a soldier with rank, fitness, and deployment status."""

    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        # store attributes so tests can access them directly
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed
        # # ensure fitness is stored as an int
        # try:
        #     self.fitness = int(fitness)
        # except (TypeError, ValueError):
        #     self.fitness = 0

    def dispatch(self):

        self.deployed = True

    def __str__(self) :
        # status = "deployed" if self.deployed else "available"
        # # return a readable single-line string (tests only require a string)
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"


if __name__ == "__main__":
    s = Soldier("Santos", "PRIVATE", 91, False)
    print(s)          

