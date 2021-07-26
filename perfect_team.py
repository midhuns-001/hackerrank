#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'perfectTeam' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING skills as parameter.
#

def perfectTeam(skills):
    dict = {"p": 0, "c":0, "m":0, "b":0, "z":0}
    for char in skills:
        if char in dict.keys():
            dict[char] = dict[char] + 1
    value_list = dict.values()
    return sorted(list(value_list))[0]
    
if __name__ == '__main__':
