#!/usr/bin/env python3

#-----------------------------------
# Title: String Formatting Lab (from lesson 3)
# Changelog:
# Aaron Devey,2019-01-28,Created
#-----------------------------------

# task 1
tuple = (2, 123.4567, 10000, 12345.67)
formatStr = "file_{:03d} :  {:.2f}, {:.2e}, {:3.2e}"
print(formatStr.format(tuple[0], tuple[1], tuple[2], tuple[3]))

# task 2
formatStr = "file_0{:02d} :  {:.2f}, {:.2e}, {:3.2e}"
print(formatStr.format(*tuple))

# task 3
def formatter(in_tuple):
  form_string = "the " + str(len(in_tuple)) + " numbers are: {:d}"
  form_string += ", {:d}" * (len(in_tuple) - 1)
  return form_string.format(*in_tuple)

print(formatter((1, 2, 3, 4, 5, 6, 7, 8)))

# task 4
tuple = ( 4, 30, 2017, 2, 27)
print("{3:02d} {4:02d} {2:02d} {0:02d} {1:02d}".format(*tuple))

# task 5
list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {list[0][:-1]} is {list[1]} and the weight of a {list[2][:-1]} is {list[3]}')
print(f'The weight of an {list[0][:-1].upper()} is {list[1] * 1.2} and the weight of a {list[2][:-1].upper()} is {list[3] * 1.2}')

# task 6
input = [['Name', 'Age', 'Cost'],
         ['Honda', '2 years', '$12345.45'],
         ['BMW', '5 years', '$9844.11'],
         ['Pontiac', '24 years', '$899.42'],
         ['Mercedes', '8 years', '$22402.84']]

str = "{:10s} {:10s} {:10s}"
for row in input:
  print(str.format(*row))
