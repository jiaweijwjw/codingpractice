#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#

# import string 
# def calc_val(word):
#     val = 0
#     for char in word:
#         if char in string.ascii_letters:
#             val += ord(char)-ord('a')
#     return val
    
# def funWithAnagrams(text):
#     # Write your code here
#     checked = {}
#     for word in text:
#         val = calc_val(word)
#         if val not in checked:
#             checked[val] = word
#     ans_dict = dict(sorted(checked.items(), key=lambda item: item[1]))
#     return [v for k, v in ans_dict.items()]
    
def funWithAnagrams(text):
    # Write your code here
    res = []
    checked = set()
    for word in text:
        sorted_word = ''.join(sorted(word)) # can replace this with frequency counting for faster time complexity and lesser space complexity
        if sorted_word not in checked:
            checked.add(sorted_word)
            res.append(word)
    res.sort()
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
