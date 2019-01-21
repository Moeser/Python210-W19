#--------------------------------
# Title: makes10 (from python pushups 2 of 2)
# Changelog:
# Aaron Devey,2019-01-20,Created
#--------------------------------

def makes10(a, b):
  if a + b == 10:
    return True
  if a == 10 or b == 10:
    return True
  return False
