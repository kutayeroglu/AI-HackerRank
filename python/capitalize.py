#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    # Split and capitalize first letter 
    splitted_name = s.split(" ")
    for part in splitted_name: 
        splitted_name[splitted_name.index(part)] = part.capitalize()
    
    # We have to return a string, construct string from list
    to_return = ""
    for s in splitted_name:
        to_return += s 
        # Add space except for the last character group
        if (splitted_name.index(s)) != -1:
            to_return += " "

    return to_return
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
