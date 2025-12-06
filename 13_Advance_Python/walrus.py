
# walrus operator (:=) allows assignment expressions within an expression.
# It was introduced in Python 3.8.

if (n := 10) > 5:
    print(f"{n} is greater than 5.")
print(f"The value of n is: {n}.")