#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'playlist' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY songs as parameter.
#

# after trying that the O(N^2) solution doesnt work below (by checking every pair combination),
# since it is too slow, then the only way is O(N) which is to try to solve it similar to two sums method which is what i initially thought of
# using a counter is just a more convenient way of using dictionary to count stuff
# the trick here is to understand the mathematics behind
# first, we must understand that we are trying to find a song1 + song1 which is a multiple of 60
# this means that (song1 + song2)%60 == 0
# by splitting
from collections import Counter
def playlist(songs):
    count = 0
    songs_counter = Counter()
    # the idea is that any multiple of 60
    for song in songs:
        other_song = -song % 60
        count += songs_counter[other_song]
        songs_counter[song % 60] += 1 # store only the reduced time
    return count
    
# def playlist(songs):
#     # Write your code here
#     songs_counter = {}
#     count = 0
#     for song in songs:
#         other_song = -song%60
#         count += songs_counter.get(0, other_song)
#         songs_counter[song%60] += 1
#     return count
 
# valid_sum = [i*60 for i in range(1, 17)]
# print(valid_sum)

# from collections import Counter
# def playlist(songs): # this doesnt work for repeated values like 60 60, since it uses a set
#     count = 0
#     songs_dict = Counter(songs)
#     songs_set = set(songs)
#     for song in songs_set.copy():
#         clone_dict = songs_dict.copy()
#         clone_dict[song] -= 1
#         for num in valid_sum:
#             rem = num - song
#             if rem in clone_dict and clone_dict[rem] >= 1:
#                 count += 1
#                 clone_dict[rem] -= 1 # think this is almost correct, just need to modify abit
#                 print(song, rem)
#         songs_set.remove(song)
#         # clone_dict.remove(song)
#     return count

# def playlist(songs): # this doesnt work for repeated values like 60 60, since it uses a set
# count = 0
# songs_set = set(songs)
# for song in songs_set.copy():
#     for num in valid_sum:
#         rem = num - song
#         if rem != song and rem in songs_set:
#             count += 1
#             print(song, rem)
#     songs_set.remove(song)
# return count
        
# def is_valid_pair(val1, val2):
#     return (val1+val2)%60 == 0

# def playlist(songs):
#     count = 0
#     # Write your code here
#     for i in range(len(songs)):
#         for j in range(i+1, len(songs)): # for the remaining on the right
#             if is_valid_pair(songs[i], songs[j]):
#                 count += 1
#     return count

# below does the same as above. what we need to do is do it faster than the combinations number of checks
# from itertools import combinations
# def playlist(songs):
#     count = 0
#     combis = combinations(songs, 2)
#     for combi in combis:
#         if sum(combi)%60 == 0:
#             count += 1
#     return count
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    songs_count = int(input().strip())

    songs = []

    for _ in range(songs_count):
        songs_item = int(input().strip())
        songs.append(songs_item)

    result = playlist(songs)

    fptr.write(str(result) + '\n')

    fptr.close()
