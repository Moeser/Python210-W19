#--------------------------------
# Title: parrot_trouble (from python pushups 2 of 2)
# Changelog:
# Aaron Devey,2019-01-20,Created
#--------------------------------

def parrot_trouble(talking, hour):
  if talking and (hour > 20 or hour < 7):
    return True
  return False
