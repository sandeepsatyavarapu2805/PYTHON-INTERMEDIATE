from dataclasses import dataclass
from typing import Tuple

# Define Type Aliases
RGB = Tuple[int, int, int]
HSL = Tuple[int, int, int]

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    # Provide default values so they are optional during instantiation
    age: int | None = None
    fav_color: RGB | None = None

def create_user(first_name: str, last_name: str, age: int | None = None, fav_color: RGB | None = None) -> User:
    email = f"{first_name.lower()}{last_name.lower()}@example.com"
    
    # Instantiate the dataclass object
    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color
    )

# Creation
user_1 = create_user('corey', 'schafer', 38, (120, 139, 219))
user_2 = create_user('john', 'doe')

print(user_1)          # Outputs a clean string: User(first_name='corey', ... )
print(user_2.email)    # johndoe@example.com