from itertools import zip_longest


list_of_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list_of_nums2 = [9, 10, 11, 12]
combined_list_of_nums = list(zip_longest(list_of_nums, list_of_nums2))

mydict = {num: num2*2 for itr1, num in enumerate(list_of_nums) for itr2, num2 in enumerate(list_of_nums2) if itr1 == itr2 }
print(mydict)
mydict2 = {num: num2 for (num, num2) in combined_list_of_nums if (num and num2) is not None}
print(combined_list_of_nums)
print(mydict2)


# custom sort: 
# <0 / -1 if x < y, x should be on the left of y
# 0 if x == y
# >0 / 1 if x > y, x should be on the right of y

# lets trying sorting a dict of tuple by the length of the string
some_names = ["james", "jiawei", "ngo", "aaron"]
some_height = [170, 180, 165, 190]
some_fruits = ["bananas", "orange", "pear", "apple"]
list_to_sort = list(zip(some_height, some_names, some_fruits))
print(list_to_sort)
dict_to_sort = {name: {"height": height, "fruit": fruit} for (height, name, fruit) in list_to_sort}
print(dict_to_sort)

# sort by length of the fruit
# .sort() only works for lists
sorted_list_dict = sorted(dict_to_sort.items(), key=lambda item : len(item[1].get("fruit")))
# print(sorted_list_dict)
sorted_dict = {name: {"height": height, "fruit": fruit} for (name, props) in sorted_list_dict for height, fruit in props.items()}
print(sorted_dict)

# sorted_list_dict = sorted(dict_to_sort.items(), key=lambda item: len(item[1]))
# sorted_list_dict = sorted(dict_to_sort.items(), key=getattr())
# sorted_dict = {name: height for (height, name) in sorted_list_dict}
# print(sorted_dict)