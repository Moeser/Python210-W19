#--------------------------------
# Title: diff21 (from python pushups 2 of 2)
# Changelog:
# Aaron Devey,2019-01-20,Created
#--------------------------------

def diff21(n):
  if n > 21:
    return((n - 21) * 2)
  return(abs(n - 21))
