#-----------------------------------
# Title: Slicing (from lesson 3)
# Changelog:
# Aaron Devey,2019-01-28,Created
#-----------------------------------

# exchanges the first and last item of a sequence
def exchange_first_last(seq):
  return seq[-1:] + seq[1:-1] + seq[0:1]

# removes every other item of a sequence
def remove_every_other_item(seq):
  return seq[0::2]

# removes the first four and last four items of a sequence
# and then returns every other item in between
def remove_first_last_four(seq):
  return seq[4:-4:2]

# reverses a sequence
def reverse(seq):
  return seq[::-1]

# splits a sequence into thirds and re-orders the thirds
def reorder_by_thirds(seq):
  return seq[int((len(seq) / 3) * 2):] + seq[:int(len(seq) / 3)] + seq[int(len(seq) / 3):int(len(seq) / 3 * -1)]


# tests
test_string = "This is a test string"
test_tuple = (99, 98, 1, 2, 0, "zero", 7, 23, 24, 5)

assert exchange_first_last(test_string) == "ghis is a test strinT"
assert exchange_first_last(test_tuple) == (5, 98, 1, 2, 0, "zero", 7, 23, 24, 99)

assert remove_every_other_item(test_string) == "Ti sats tig"
assert remove_every_other_item(test_tuple) == (99, 1, 0, 7, 24)

assert remove_first_last_four(test_string) == " sats t"
assert remove_first_last_four(test_tuple) == (0,)

assert reverse(test_string) == "gnirts tset a si sihT"
assert reverse(test_tuple) == (5, 24, 23, 7, "zero", 0, 2, 1, 98, 99)

assert reorder_by_thirds(test_string) == " stringThis is a test"
assert reorder_by_thirds(test_tuple) == (7, 23, 24, 5, 99, 98, 1, 2, 0, 'zero', 7)

print("Tests passed")
