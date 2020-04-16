#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    # what are the choices
    plays = ['rock', 'paper', 'scissors']
    awnser = []
    round_count = 0
    #iterate over the choices that could be made
    if n == 0:
        return [ []]
    else:
        for x in plays:
            print("For x in plays ran")
            if True:
                awnser.append([])
                awnser[round_count].append(x)
                if len(awnser[round_count]) == n:
                    round_count += 1
                    print("next set")
                print("if True Ran")
        # terminate and reducse as the rounds take place
        print(awnser)
        return awnser


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


test = 1
print(rock_paper_scissors( test))
