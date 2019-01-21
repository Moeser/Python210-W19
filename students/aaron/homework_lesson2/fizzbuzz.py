#----------------------------------#
# Title: Fizz Buzz (from lesson 2)
# Changelog:
# Aaron Devey,2019-01-20,Created
#----------------------------------#


'''
   fizzbuzz(n):  return a number (as a str), or return Fizz, or Buzz, or FizzBuzz for multiples of 3, 5, or 15 respectively.
   n: the number to return
   returns: string
'''
def fizzbuzz(n):
  if n % 15 == 0:
    return("FizzBuzz")
  if n % 5 == 0:
    return("Buzz")
  if n % 3 == 0:
    return("Fizz")
  return(str(n))


''' The instructions specifically want 1 through 100, so range(1, 101) is exactly that. '''
for n in range(1, 101):
  print(fizzbuzz(n))

