# Composed Object 1
class CombustionEngine:

    def spark(self) -> str:
        return "vroom vroom"


# Composed Object 2
class ElectricMotor:

    def spark(self) -> str:
        return "silent hum"


# Unified Class using Composition
class Car:

    def __init__(self, model: str, propulsion_system):
        self.model = model
        self.engine = propulsion_system  # Composition: Car 'has a' propulsion system

    def drive(self) -> str:
        # Polymorphism: Calls .spark() regardless of the object type passed in
        return f"{self.model} goes {self.engine.spark()}"


# --- Execution ---
print("--- Group 4: Composition & Polymorphism ---")

gas_car = Car("Mustang", CombustionEngine())
ev_car = Car("Model 3", ElectricMotor())

# Polymorphic behavior in action
fleet = [gas_car, ev_car]
for vehicle in fleet:
    print(vehicle.drive())