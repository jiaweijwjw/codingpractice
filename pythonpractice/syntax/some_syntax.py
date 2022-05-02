# imports
from itertools import zip_longest, chain

# list comprehension, or just comprehension in general
base_list = [0, 1, 2, 3, 4, 5, 6, 7]
squared_base_list = [num**2 for num in base_list]
# [output if condition else output for l in list]

# combining 2 lists into single list of 2-tups
class CombineTwoList:
    def __init__(self, list1, list2) -> None:
        self.list1 = list1
        self.list2 = list2
        self.combined_list = []

    def print_combined_list(self):
        print(self.combined_list)

    def set_lists(self, new_list1, new_list2):
        self.list1 = new_list1
        self.list2 = new_list2

    def combine_manually(self):
        self.combined_list = []
        if not self.list1 and not self.list2: # both lists empty
            self.combined_list = []
        elif not self.list1: 
            self.combined_list = [(None, num) for num in self.list2]
        elif not self.list2:
            self.combined_list = [(num, None) for num in self.list1]
        else:
            len_list1 = len(self.list1)
            len_list2 = len(self.list2)
            min_len = min(len_list1, len_list2)
            max_len = max(len_list1, len_list2)
            for i in range(0, min_len):
                self.combined_list.append((self.list1[i], self.list2[i]))
                if i == min_len - 1 and len_list1 != len_list2:
                    y = min_len
                    while y < max_len:
                        if len_list1 > len_list2:
                            self.combined_list.append((self.list1[y], None))
                        else:
                            self.combined_list.append((None, self.list2[y]))
                        y += 1
        
    def combine_zip(self):
        # this only combines up till the length of the shortest list, similar to the map version
        self.combined_list = list(zip(self.list1, self.list2))

    def combine_zip_longest(self):
        # this combines till the end of the longer list, similar to the manual version
        self.combined_list = list(zip_longest(self.list1, self.list2, fillvalue="_"))

    def combine_map(self):
        self.combined_list = list(map(lambda x, y: (x, y), self.list1, self.list2))
                


# some string manipulations
a_string = "helloworld"
list_of_strings = ["hello", "world", "thailand"]

# making each char in a string as an element in a list
charlist_a_string = list(a_string)
charlist_a_string2 = [char for char in a_string] # list comprehension version also works

# doing the same as above, but for chars of all strings in a list
list_of_charlist = list(map(list, list_of_strings))
list_of_charlist2 = list(map(lambda string: [char for char in string], list_of_strings))

# assigning string value to another variable
another_string = "".join(a_string)
yet_another_string = a_string[:]
combined_string = a_string + another_string

# appending / combining lists
some_list = base_list + squared_base_list
base_list.extend(squared_base_list) # modifies the original base_list
copied_list = base_list[:] # copy
pointer_list = base_list # pointer
