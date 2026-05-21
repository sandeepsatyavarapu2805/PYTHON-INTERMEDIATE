class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner  # Public attribute
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = balance  # Private attribute (Name mangling applies)

    # The Property also changes the calling of the method like an attribute so like sccount.balance without ()
    # Property Getter
    @property
    def balance(self) -> float:
        return self.__balance

    # Property Setter
    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            print("[ERROR] Cannot set a negative balance!")
        else:
            self.__balance = amount

print("--- Group 2: Encapsulation & Properties ---")
account = BankAccount("Alice", 1000.0)

# Direct access to __balance causes an AttributeError
print(f"Account Owner: {account.owner}")
try:
    print(account.__balance)
except AttributeError:
    print("[SUCCESS] __balance is protected and not directly accessible.")

print(f"Current Balance (via getter): ${account.balance}")

# Modifying data via the property setter
account.balance = 1500.0
print(f"Updated Balance: ${account.balance}")

account.balance = -500.0  # Invalid update caught by setter
print()