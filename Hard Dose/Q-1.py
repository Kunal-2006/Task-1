# hard_dose_1.py

# Size of the grid
SIZE = 11

# Make an empty 11x11 grid with all 1s (safe spots)
grid = []
for i in range(SIZE):
    row = []
    for j in range(SIZE):
        row.append(1)
    grid.append(row)

file = open(file_name, "r")
lines = file.readlines()
file.close()


input(int("enter the number of rows"))
