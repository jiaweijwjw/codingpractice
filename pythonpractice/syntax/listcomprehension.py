from itertools import zip_longest, chain

# testing list comprehension

list0 = [0, 1, 2, 3, 4, 5, 6]


list1 = []

for i in range(0, 5):
    list1.append(i*2)

list2 = [i*2 for i in range(0, 5)] # list comprehension
list3 = [num*2 for num in list0 if num <= 4]
list4 = [(x, y) for x in list2 for y in list3]
# list5 = [(x, y) for x in list2 and not list3 for y in list3 and not list2]
# print(list5)
# dict1 = {num: num*2 for num in list0}
# print(dict1)


# combining 2 lists into a list of 2-tup

# naive
# print(list0)
len_list0 = len(list0)
# print(len_list0)
# print(list3)
len_list3 = len(list3)
# print(len_list3)

merged_list = []

for i in range(0, min(len_list0, len_list3)): # add everything from the starting
    merged_list.append((list0[i], list3[i]))
    if i == min(len_list0, len_list3)-1 and len_list0 != len_list3:
        y = min(len_list0, len_list3)
        while y < max(len_list0, len_list3):
            if len_list0 > len_list3:
                merged_list.append((list0[y], None))
            elif len_list0 < len_list3:
                merged_list.append((None, list3[y]))
            y += 1
        

# print(merged_list)

# zip
zippedlist3 = zip(list3, list0)
print(zippedlist3)
print(list(zippedlist3))

# enumerate
merged_list_enumerate = [(x, y) for itr_x, x in enumerate(list0) for itr_y, y in enumerate(list3) if itr_x == itr_y]
print(merged_list_enumerate)

# following doesnt work because the iterators move one by one
# merged_list_enumerate2 = [(x, y) if itr_x == itr_y else ((x, None) if itr_x > itr_x and itr_x == len(list0)-1 else ((None, y) if itr_y > itr_x and itr_y == len(list3)-1 else (None, None) ) ) for itr_x, x in enumerate(list0) for itr_y, y in enumerate(list3)]
# print(merged_list_enumerate2)
# merged_list_enumerate3 = [(x, None) if itr_x > itr_y and itr_y == len(list3) else (None, y) if itr_y > itr_x and itr_x == len(list0) else (x, y) for itr_x, x in enumerate(list0) for itr_y, y in enumerate(list3)]
# print(merged_list_enumerate3)
# print(len(merged_list_enumerate3))
merged_list_enumerate4 = zip_longest(list3, list0)
merged_list_enumerate5 = zip_longest(list3, list0, fillvalue="_")
print(list(merged_list_enumerate4))
print(list(merged_list_enumerate5))

# map
merged_list_map = list(map(lambda x, y: (x, y), list0, list3)) # can take in 2 iterables
print(merged_list_map)

string0 = "helloworld"
list6 = list(string0)
list_of_strings = ["hello", "world", "thailand"]
list7 = list(map(list, list_of_strings))
print(list7)

combined_list0 = list0 + list3
print(combined_list0)
combined_list1 = list(chain(list0, list3))
print(combined_list1)
list0.extend(list3)
combined_list2 = list0[:] # copy
combined_list3 = list0 # pointer
print(combined_list2 is list0)
print(combined_list3 is list0)

string1 = "".join(string0)
string2 = string0[:]
print(string1 is string0)
print(string2 is string0)
