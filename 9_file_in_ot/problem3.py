# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year old. 

def generate_table(n):
    table = " "
    folder ="tables/"
    for a in range(1, 11):
        table +=(f"{n} x {a} = {n * a}\n")
    with open(f"{folder}table_{n}.txt", "w") as file:
        file.write(table)


for a in range(2, 21):
    generate_table(a)
