
# advance type hints in python used to specify more complex data types and structures.

from typing import List, Dict, Tuple, Optional, Union

# List type hint
numbers: List[int] = [1, 2, 3, 4 ]

# Dictinonary type hint
user_info: Dict[str, int] = {"name": "Karan", "age": 25}

# Tuple type hint
canditaes : Tuple[str, int ] = ("Partiyush", 24)


# Optional type hint

def get_user_age(user: Dict[str, Union[str, int]]) -> Optional[int]:
    return user.get("age")   
       
print(get_user_age(user_info))  
