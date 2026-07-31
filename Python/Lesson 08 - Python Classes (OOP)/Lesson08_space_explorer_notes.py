# class Spacecraft():
#     def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
#         self.name = name
#         self.fuel_level = fuel_level
#         self.fuel_efficiency = fuel_efficiency

#     def add_fuel(self, amount: float) -> None:
#         self.fuel_level += amount

#     def calculate_required_fuel(self, distance: float) -> float:
#         return distance / self.fuel_efficiency

#     def check_fuel(self, distance: float) -> bool:
#         return self.fuel_level >= self.calculate_required_fuel(distance)

#     def launch(self, distance: float) -> None:
#         if self.check_fuel(distance):
#             self.fuel_level -= self.calculate_required_fuel(distance)
#             print(f"{self.name} has successfully traveled {distance} units!")
#         else:
#             print(f"{self.name} does not have enough fuel to travel {distance} units.")
            
            
# galactica = Spacecraft(name="Galactica", fuel_level=75.0, fuel_efficiency=22.0)
# galactica.add_fuel(20)
   
class Spacecraft():
    
    def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency
        self.max_fuel = 200000

    def add_fuel(self, amount: float) -> None:
        self.fuel_level = min(self.fuel_level + amount, self.max_fuel)
        self.fuel_level = max(self.fuel_level, 0)
        
    def fuel_required(self, distance):
        amount = distance / self.fuel_efficiency
        return amount
    
    def fuel_available(self, distance):
        return self.fuel_level >= self.fuel_required(distance)
    
    def launch(self, distance):
        if self.fuel_available(distance):
            self.fuel_level -= self.fuel_required(distance)
            print(f"{self.name} has successfully traveled {distance} miles!")
        else:
            print(f"{self.name} does not have enough fuel to travel {distance} miles.")
            
    def calculate_required_fuel(self, distance: float) -> float:
        return distance / self.fuel_efficiency

    def check_fuel(self, distance: float) -> bool:
        return self.fuel_level >= self.calculate_required_fuel(distance)

    # def launch(self, distance: float) -> None:
    #     if self.check_fuel(distance):
    #         self.fuel_level -= self.calculate_required_fuel(distance)
    #         print(f"{self.name} has successfully traveled {distance} units!")
    #     else:
    #         print(f"{self.name} does not have enough fuel to travel {distance} units.")
    
    
sp1 = Spacecraft("Vostok 1", 250, 1.5)
sp2 = Spacecraft("Vostok 2", 400, 2.0)
sp3 = Spacecraft("Apollo 11", 600, 2.5)
sp1.launch(400)
sp2.launch(200)
sp3.launch(300)   