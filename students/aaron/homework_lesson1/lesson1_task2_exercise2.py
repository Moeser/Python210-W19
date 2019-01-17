#--------------------
# Title: Lesson 1, Task 2, Exercise 2 (Codingbat Warmup-1: monkey_trouble)
# Changelog:
# Aaron Devey,2019-01-12,New File
#---------------------

def monkey_trouble(a_smile, b_smile):
  # using xor since it fits well here
  return not (a_smile ^ b_smile)
