#!/usr/bin/env python3

#---------------------------------
# Title: List Lab (from lesson 3 homework)
# Changelog:
# Aaron Devey,2019-01-29,Created
#---------------------------------


# Series 1
originalFruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits = originalFruits.copy()
print(fruits)
fruits = fruits + [input("Enter a new fruit: ")]
print(fruits)
index = input("Enter a fruit number (1 indexed): ")
print("You entered: " + fruits[int(index) - 1])
fruits = ["Bananas"] + fruits
print(fruits)
fruits.insert(0, "Honeydew")
print(fruits)
for fruit in fruits:
  if fruit[0] == "P":
    print(fruit)

# Series 2
print(fruits)
fruits = fruits[:-1]
print(fruits)
deleted = False

## bonus: multiply list * 2 and keep asking.
## using a copy here or it messes up Series 3.
fruitsCopy = fruits.copy()
while not deleted:
  fruitsCopy = fruitsCopy + fruitsCopy
  toDelete = input("Enter a fruit to delete: ").lower()
  for fruit in fruitsCopy:
    if fruit.lower() == toDelete:
      deleted = True
      fruitsCopy.remove(fruit)

# Series 3
for fruit in fruits.copy():
  like = "maybe"
  while like != "yes" and like != "no":
    like = input("Do you like " + fruit.lower() + "? ").lower()
    if like == "no":
      fruits.remove(fruit)
    elif like != "yes":
      print("This is a yes or no question, try again.")

print(fruits)

# Series 4
newFruits = []
for fruit in originalFruits:
  newFruits += [fruit[::-1]]

newFruits = newFruits[:-1]
print("Original: " + str(originalFruits))
print("Copy: " + str(newFruits))
