from abc import ABC, abstractmethod


# 1. Abstraction: Defining a blueprint template
class Vehicle(ABC):

    def __init__(self, brand: str):
        self.brand = brand

    @abstractmethod
    def start_engine(self) -> str:
        """Abstract method; must be implemented by subclasses."""
        pass


# 2. Inheritance: Reusing base functionality and implementing abstract contracts
class ElectricCar(Vehicle):

    def start_engine(self) -> str:
        return f"{self.brand} silent motor started smoothly."


class Truck(Vehicle):

    def start_engine(self) -> str:
        return f"{self.brand} heavy diesel engine roars to life."


# --- Execution ---
print("--- Group 3: Abstraction & Inheritance ---")

# Cannot instantiate an abstract class directly
try:
    v = Vehicle("Generic")
except TypeError:
    print("[SUCCESS] Cannot instantiate abstract class Vehicle directly.")

# Instantiating concrete children
tesla = ElectricCar("Tesla")
scania = Truck("Scania")

print(tesla.start_engine())
print(scania.start_engine())
print()