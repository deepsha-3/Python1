

# Example of match-case statement in Python.

def weekday_name(day_number):
    match day_number:
       case 1:
            return "Sunday"
       case 2:
            return "Monday"
       case 3:
            return "Tuesday"
       case 4:
            return "Wednesday"
       case 5:
            return "Thursday"
       case 6:
            return "Friday"
       case 7:
            return "Saturday"
       
    

if __name__ == "__main__":
    for i in range(1, 9):
        print(f"Day {i}: {weekday_name(i)}")