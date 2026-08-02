# # class Spacecraft:
# #     def __init__(self, name:str, fuel_level:float, fuel_efficiency:float):
# #         self.name = name
# #         self.fuel_level = fuel_level
# #         self.fuel_efficiency = fuel_efficiency

# #   #method add fuel
# #     def add_fuel(self, amount:float):
# #         self.fuel_level += amount

# #   #calculate the fuel required for a given distance
# #     def fuel_required (self, distance:float):
# #         return distance /self.fuel_efficiency

# #   #check if enough fuel is available to travel that distance
# #     def check_fuel (self, distance:float):
# #         return self.fuel_level >= self.fuel_required(distance)
    
# #   #Launch the spacecraft and deduct fuel if successul
# #     def launch (self, distance:float ):
# #         if self.check_fuel(distance):
# #                     self.fuel_level -= self.fuel_required(distance)
# #                     print(f"{self.name} has successfully traveled {distance} units!")
# #         else:
# #                     print(f"{self.name} does not have enough fuel to travel {distance} units.")



# # if __name__ == "__main__":
# #     test_craft = Spacecraft("Testing", 1000, 0.50)  # new spacecraft
# #     print(test_craft.fuel_required(100))            # should be 200
# #     print(test_craft.check_fuel(1000))              # should be false
# #     test_craft.launch(500)                          # should work
# #     print(test_craft.fuel_level)                    # should be 0

# # class Spacecraft:
# #     def __init__(self, name:str, fuel_level:float, fuel_efficiency:float):
# #         self.name = name
# #         self.fuel_level = fuel_level
# #         self.fuel_efficiency = fuel_efficiency
# #         self.max_fuel = 200_000

# #     def add_fuel(self, quantity):
# #         self.fuel_level = min(self.max_fuel, self.fuel_level + quantity)
# #         self.fuel_level = max(self.fuel_level, 0)

# #     def fuel_required(self, distance):
# #         amount = distance / self.fuel_efficiency
# #         return amount

# #     def fuel_available(self, distance):
# #         return self.fuel_level >= self.fuel_required(distance)

# #     def launch(self, distance: float) -> None:
# #             if self.check_fuel(distance):
# #                 self.fuel_level -= self.calculate_required_fuel(distance)
# #                 print(f"{self.name} has successfully traveled {distance} units!")
# #             else:
# #                 print(f"{self.name} does not have enough fuel to travel {distance} units.")

# # sp1=Spacecraft("Vostok 1", 250, 1.5)
# # sp2=Spacecraft("Voyager 1", 400, 2.0)
# # sp3=Spacecraft("Apollo 11", 600, 2.5)

# import math
# class Planet:
#     def __init__(
#             self, name:str, 
#             coordinates:tuple [float, float, float], 
#             danger:float, 
#             resources: float, 
#             atmosphere:str):
        
#             self.name = name
#             self.coordinates = coordinates  
#             self.danger = danger
#             self.resources = resources
#             self.atmosphere = atmosphere

#     def __str__(self):
#             x,y,z = self.coordinates
#             return (f"Planet: {self.name}\n"
#             f"Coordinates: x:{x},y:{y},z:{z}\n"
#             f"Danger: {self.danger}\n"
#             f"Resources: {self.resources}\n"
#             f"Atmosphere: {self.atmosphere}\n"
#                 )

#     def __sub__(self, planetx):
#         if not isinstance(planetx, Planet): #to make sure it's a planet
#             return TypeError("Must only substract planet")
#         x1, y1, z1 = self.coordinates
#         x2, y2, z2 = planetx.coordinates
#         return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

        


# p1 = Planet("Mars", (1, 2, 3), 5, 100, "Thin carbon dioxide")
# p2 = Planet("Earth", (4, 6, 15), 2, 500, "Nitrogen and oxygen")
# print(p2)

# distance = p2 - p1 
# print(f"Distance: {distance}")


# def palindrome (input_str):
#     if input_str == "":
#         return True

#     if input_str[0] != input_str[-1]:
#         return False
    
#     print(f"computing {}")
#     return palindrome (input_str[1:1-1])

# print(palindrome('level'))
# print(palindrome("3335"))

#Calculate the sum of a list of numbers using recursion 

def list_sum(numbers):
   # Base case: if the list is empty, return 0
   if not numbers:
       return 0
   
   # Recursive case: sum first element with sum of the rest
   return numbers[0] + list_sum(numbers[1:])


print(list_sum([1, 2, 3, 4, 5,6,7,8,9]))