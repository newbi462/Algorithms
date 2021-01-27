#!/usr/bin/python

import sys
import math

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

  # what math groups to families of those base cases
  #what conditions shouold math repeate those groupings

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


"""
class code:

1
___
1

2
___
1,1
2

3
___
1,1,1
2,1
1,2
3

4
___
1,1,1,1


5
___
1,1,1,1,1
1,1,1,2
1,1,2,1
1,2,1,1
2,1,1,1
1,1,3
1,3,1
3,1,1
2,1,2
1,2,2
2,2,1
2,3
3,2


5 = solutions 4 + solutions 3 + solutions 2, so fib like
return eating_cookies(n - 1 + eating_cookies(n - 2) + eating_cookies(n - 3)

def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

"""
