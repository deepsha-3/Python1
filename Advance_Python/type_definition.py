
# Type definitions in Python allow you to specify the expected data types of variables, function parameters, and return values.

# This helps improve code readability and can catch type-related errors during development.

num : int = 10
name : str = "Deepsha"
def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"

print(greet(name))

