from itertools import zip_longest


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

list6 = list(map(lambda num: num*2, list0))

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
# following doesnt work because the iterators move one by one
merged_list_enumerate2 = [(x, y) if itr_x == itr_y else (x, None) if itr_x > itr_y else (None, y) for itr_x, x in enumerate(list0) for itr_y, y in enumerate(list3)]
print(merged_list_enumerate)
# print(merged_list_enumerate2)
merged_list_enumerate3 = [(x, None) if itr_x > itr_y and itr_y == len(list3) else (None, y) if itr_y > itr_x and itr_x == len(list0) else (x, y) for itr_x, x in enumerate(list0) for itr_y, y in enumerate(list3)]
# print(merged_list_enumerate3)
print(len(merged_list_enumerate3))
merged_list_enumerate4 = zip_longest(list3, list0)
print(list(merged_list_enumerate4))