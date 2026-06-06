from typing import Tuple, TypedDict, NotRequired

# Define Type Aliases
RGB = Tuple[int, int, int]
HSL = Tuple[int, int, int]

class User(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: NotRequired[int | None]
    fav_color: NotRequired[RGB | None]

def create_user(first_name: str, last_name: str, age: int | None = None, fav_color: RGB | None = None) -> User:
    email = f"{first_name.lower()}{last_name.lower()}@example.com"
    
    # Construct a plain dictionary
    user: User = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
    }
    
    # Only add NotRequired keys if they are provided
    if age is not None:
        user['age'] = age
    if fav_color is not None:
        user['fav_color'] = fav_color
        
    return user

# Creation
user_1 = create_user('corey', 'schafer', 38, (120, 139, 219))
user_2 = create_user('john', 'doe')

# Accessing values (Key notation)
print(user_1)          # Outputs raw dict: {'first_name': 'corey', ...}
print(user_2['email']) # johndoe@example.com