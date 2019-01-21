#---------------------------------
# Title: grid_printer (from lesson 2)
# Changelog:
# Aaron Devey,2019-01-20,Created
#---------------------------------

''' Note: The definition of the side of a cell is re-defined in a different
    way 3 separate times in this assignment.  Since it's not consistent,
    just trying to make a good approximation of what they're looking for
    here based on part 3.
'''

# prints a seperator or bottom/top row
def print_seperator(cells, size):
  line = ""
  for i in range(cells):
    line += "+" + " -" * size + " "
  line += "+"
  print(line)

# prints a line that forms a cell
def print_line(cells, size):
  line = ""
  for i in range(cells):
    line += "|" + "  " * size + " "
  line += "|"
  print(line)

# from part2, prints a 2x2 grid with cells of "size"
def print_grid(size):
  for height in range(2):
    print_seperator(2, size)
    for lines in range(size):
      print_line(2, size)
  print_seperator(2, size)

# from part3, prints a grid of (cells)*(cells) and each cell sized at "size"
def print_grid2(cells, size):
  for height in range(cells):
    print_seperator(cells, size)
    for i in range(size):
      print_line(cells, size)
  print_seperator(cells, size)
 
# from part1, prints a static grid
def static_grid():
  print('''+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +''')

static_grid()
print_grid(3)
print_grid(15)
print_grid2(5, 3)
