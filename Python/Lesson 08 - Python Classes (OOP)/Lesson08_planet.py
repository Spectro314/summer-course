import random

class Planet():
    def __init__(self, name: str, coordinates: tuple[float, float, float], danger: float, resources: float, atmosphere: str):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere
        
        self.max_missions = max(1, 4 - int(self.danger))
        self.missions_done: dict[str, int] = {}

    def __str__(self) -> str:
        return (f"{self.name} - Coordinates: ({self.coordinates[0]}, {self.coordinates[1]}, {self.coordinates[2]}), Danger: {self.danger}, Resources: {self.resources}, Atmosphere: {self.atmosphere}")

    def __sub__(self, other) -> float:
        diff = tuple(coord_1 - coord_2 for coord_1, coord_2 in zip(self.coordinates, other.coordinates))
        return (diff[0] ** 2 + diff[1] ** 2 + diff[2] ** 2) ** 0.5

    def can_do_mission(self, player_name: str) -> bool:
        return self.missions_done.get(player_name, 0) < self.max_missions

    def record_mission(self, player_name: str) -> None:
        self.missions_done[player_name] = self.missions_done.get(player_name, 0) + 1

    def mission_success(self) -> tuple[str, float]:
        chance = max(0.2, 1.0 - 0.15 * self.danger)
        roll = random.random()
        if roll < chance:
            return "success", self.resources
        elif roll < chance + 0.2:
            return "partial", self.resources // 2
        else:
            return "fail", 0
 
if __name__ == "__main__":
#    print(p1 - p2)
    print(p1)
    print(p2)
    
        
p1 = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
p2 = Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
p3 = Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
p4 = Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
p5 = Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
p6 = Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
p7 = Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
p8 = Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
p9 = Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
p10 = Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")

print(Planet)

