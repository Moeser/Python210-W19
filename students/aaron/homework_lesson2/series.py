#-----------------------------------#
# Title: series.py (from lesson 2)
# Changelog:
# Aaron Devey,2019-01-20,Created
#-----------------------------------#
'''
    note: For each function I used a cache, for fun.  I was noticing
    that a large number of the recursive calls run multiple times,
    and that the functions could be made more efficient with a cache.
'''


'''
   fibonacci(n): calculate the Nth index of the fibonacci sequence
   n: the desired index of the fibonacci squence
   returns: int
'''
fibCache = {0: 0, 1: 1}
def fibonacci(n):
  if n in fibCache:
    return fibCache[n]
  fibCache[n] = fibonacci(n - 1) + fibonacci(n - 2)
  return fibCache[n]

'''
   lucas(n): calculate the Nth index of the lucas sequence
   n: the desired index of the lucas squence
   returns: int
'''
lucasCache = {0: 2, 1: 1}
def lucas(n):
  if n in lucasCache:
    return lucasCache[n]
  lucasCache[n] = lucas(n - 1) + lucas(n - 2)
  return lucasCache[n]

'''
   sum_series(n, [n0, [n1]]): calculate the Nth index of the fibonacci-like sequence
   n: the desired index of the series
   n0: the pre-defined index at 0
   n1: the pre-defined index at 1
   returns: int
   note: defaults to the fibonacci sequence
'''
cache = {0: 0, 1: 1}
def sum_series(n, n0=0, n1=1):
  # reset the cache if the starting values differ
  if cache[0] != n0 or cache[1] != n1:
    cache.clear()
    cache[0] = n0
    cache[1] = n1
  if n in cache:
    return cache[n]
  cache[n] = sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)
  return cache[n]


# tests
if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
