
# advance type hints in python used to specify more complex data types and structures.

from typing import List, Dict, Tuple, Optional, Union

# List type hint
numbers: List[int] = [1, 2, 3, 4 ]
print("List:", numbers)

# Dictinonary type hint
user_info: Dict[str, int] = {"name": "Karan", "age": 25}
print("Dictionary:", user_info)

# Tuple type hint
canditaes : Tuple[str, int ] = ("Partiyush", 24)
print("Tuple:", canditaes)


# Optional type hint

def get_user_age(user: Dict[str, Union[str, int]]) -> Optional[int]:
    return user.get("age")   
       
print(get_user_age(user_info))  

# Union type hint
id : Union[int, str] = " ABC123"
print(id) 