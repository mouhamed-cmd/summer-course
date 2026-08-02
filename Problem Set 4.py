# problem 1
class Soldier:
    """Represents a soldier with rank, fitness, and deployment status."""

    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        # store passed values on the instance
        self.name = name
        self.rank = rank
        self.fitness = int(fitness)
        self.deployed = bool(deployed)

    def dispatch(self) -> None:
        """Mark this soldier as deployed."""
        self.deployed = True

    def __str__(self) -> str:
        # match the report format used elsewhere in the repo/tests
        status = "deployed" if self.deployed else "available"
        return f"{self.name} | {self.rank} | Fitness:{self.fitness} | Status:{status}"


def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
    """Parse report strings and return (roster_dict, ranks_set)."""
    roster: dict[str, Soldier] = {}
    ranks: set[str] = set()

    for report in report_list:
        # expected format: "NAME | Rank | Fitness:NN | Status:available"
        parts = [p.strip() for p in report.split("|")]
        if len(parts) < 4:
            # skip malformed lines
            continue
        name = parts[0]
        rank = parts[1]
        # parts[2] expected "Fitness:NN"
        fitness_part = parts[2].split(":", 1)
        fitness = int(fitness_part[1].strip()) if len(fitness_part) > 1 else 0
        # parts[3] expected "Status:available" or "Status:deployed"
        status_part = parts[3].split(":", 1)
        status = status_part[1].strip().lower() if len(status_part) > 1 else "available"
        deployed = status == "deployed"

        soldier = Soldier(name, rank, fitness, deployed)
        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    available = [name for name, s in roster.items() if not s.deployed]
    for name in sorted(available):
        print(name)


def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    if name not in roster:
        print(f"Soldier {name} not found")
        return

    soldier = roster[name]
    if soldier.deployed:
        print(f"{name} is already deployed")
    else:
        soldier.dispatch()


def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    bands = {"high": [], "medium": [], "low": []}
    for name, s in roster.items():
        if s.fitness >= 80:
            bands["high"].append(name)
        elif s.fitness >= 60:
            bands["medium"].append(name)
        else:
            bands["low"].append(name)

    # keep list order deterministic for tests
    for k in bands:
        bands[k].sort()
    return bands
