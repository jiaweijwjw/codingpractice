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
import string 
def calc_val(word):
    val = 0
    # the val could be too large, maybe we can try using dict. since only a-z, the dict can be considered a constant
    for char in word:
        if char in string.ascii_letters:
            val += ord(char)-ord('a')
    return val

# def get_char_dict(word):
#     char_dict = {}
#     for char in word:
#         if char not in char_dict:
#             char_dict[char] = 1
#         else:
#             char_dict[char] += 1

def funWithAnagrams(text):
    # Write your code here
    checked = {}
    for word in text:
        val = calc_val(word)
        if val not in checked:
            checked[val] = word
    ans_dict = dict(sorted(checked.items(), key=lambda item: item[1]))
    return [v for k, v in ans_dict.items()]

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
