# you can use this variable to test problems independently
# while you're working locally
TESTING_PROBLEM = 1


# problem 1
def process_reports(report_list: list[str]) -> tuple:
    pass


def show_available(roster: dict[str, dict[str, object]]) -> None:
    pass


def dispatch(roster: dict[str, dict[str, object]], name: str) -> None:
    pass


def fitness_report(roster: dict[str, dict[str, object]]) -> dict[str, list[str]]:
    pass


# problem 2

# problem 3

# problem 4

# This will only execute if this script is executed directly, not imported
if __name__ == "__main__":
    if TESTING_PROBLEM == 1:
        reports = [
            "SANTOS | Private | Fitness:91 | Status:available",
            "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
            "OKAFOR | Sergeant | Fitness:88 | Status:available",
            "BRIGGS | Private | Fitness:55 | Status:available",
            "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
            "REYES | Sergeant | Fitness:79 | Status:available",
        ]

        # add your own testing here for problem 1

    elif TESTING_PROBLEM == 2:
        pass

    elif TESTING_PROBLEM == 3:
        pass

    elif TESTING_PROBLEM == 4:
        pass

    else:
        print("There are only 4 problems!")
