#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = ' ' + s
    r = ''
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and s[i] != ' ':
            r += s[i].upper()
        else:
            r += s[i]
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
