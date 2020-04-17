#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    # what are the choices
    plays = ['rock', 'paper', 'scissors']
    #choice_sets = []
    #for x in plays:
        #choice_set.append(x) * n
        #print(choice_set)
    awnser = []
    #round_count = 0
    #iterate over the choices that could be made
    if n == 0:
        return [[]]
    else:
        def recursive(round_count, choice_set):
            #foo = []
            for x in plays:
                choice_set.append(x)
                if round_count == n:
                    #print(x)
                    #print(f"{spaces(n*2)} {x}")
                    #print(f"{spaces(n*2)}done")
                    #print(f"{spaces(n*2)} awnser before:{awnser}")
                    #print(f"awnser before:{awnser}")
                    awnser.append([*choice_set]) # when  apending a [] you usy * ity in to make a copy and unlink mem
                    #print(f"{spaces(n*2)}choice_set is:{choice_set}")
                    #print(f"choice_set is:{choice_set}")
                    #print(f"{spaces(n*2)}awnser after:{awnser}\n")
                    #print(f"awnser after:{awnser}\n")
                    #return awnser
                    #nonlocal awnser.append([*awnser])
                else:
                    #print(f"{spaces(n*2)}awnser before recuse:{awnser}")
                    #print(f"awnser before recuse:{awnser}")
                    recursive(round_count + 1, choice_set)
                    #print(f"this is foo: {foo}")
                    #print(f"round: {round_count}")
                    #print(f"choice_set: {choice_set}")
                #print(len(choice_set)-1)
                del choice_set[-1]
                #print(f"awnser 3:{awnser}")
            return awnser

        #print(f"awnser 1:{awnser}")
        recursive(1, [])
        #print(f"awnser 2:{awnser}")
        return awnser


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


test = 2
print(rock_paper_scissors( test))
