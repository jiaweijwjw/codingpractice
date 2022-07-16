import pprint

names = ["James", "Aaron", "Jiawei"]
ages = [24, 25, 26]
height = [170, 180, 190]
weight = [80, 70, 60]
people = list(zip(names, ages))
people2 = [(name, age) for name in names for age in ages] # list comprehension uses nested loop / double for loop semantics
profiles = [{"name": name, "age": age, "height": h, "weight": w} for (name, age, h, w) in list(zip(names, ages, height, weight))]
print(f"people: {people}")
pprint.pprint(profiles)
# print(f"people2: {people2}")
print()

def compare_by_age(x):
    # x is tuple of (name, age)
    return x[1]

# list.sort() is in place
def using_list_sort(my_list):
    clone_my_list = my_list[:]
    clone_my_list.sort()
    print(clone_my_list)
    print()

# sorted function copies the original list
def using_sorted(my_list):
    sorted_list = sorted(my_list)
    print(sorted_list)
    print()

# by default, the first element of the tuple is used for comparison.
# and since names are strings, there are sorted by alphabetical order
# by default, the order is ascending order
# now we will try to sort by the second element in the tuple which is the age
# to do custom comparison, we will have to use our own compare function as the key argument to the sorted() function or list.sort() method
def sort_by_second_tup_el(my_list):
    sorted_list = sorted(my_list, key=compare_by_age) # since it is only a one liner, we can use a lambda as below
    print(sorted_list)
    print()

# try using lambda function for the same functionality above
def sort_by_second_tup_el_using_lambda(my_list):
    sorted_list = sorted(my_list, key=lambda x: x[1])
    print(sorted_list)
    reverse_sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)
    print(reverse_sorted_list)
    print()


# we will try to sort the list of dictionaries too
def sort_by_dict_value(my_list, key):
    sorted_list = sorted(my_list, key=lambda x: x.get(key))
    print(f"by {key}")
    pprint.pprint(sorted_list)
    print()


# then now we will try to sort by the other third character in the name
# also showing if this works for list.sort() too? YES it does
def sort_descending_by_third_char_in_name(my_list): # please ensure that the names are at least 3 characters long for this testing
    clone_list = my_list[:]
    clone_list.sort(key=lambda x: x.get("name")[2], reverse=True)
    pprint.pprint(clone_list)
    print()

if __name__ == "__main__":
    # using_list_sort(people)
    # using_sorted(people)
    # sort_by_second_el(people)
    # sort_by_second_tup_el_using_lambda(people)
    # for key in ["name", "age", "height", "weight"]:
    #     sort_by_dict_value(profiles, key)
    sort_descending_by_third_char_in_name(profiles)