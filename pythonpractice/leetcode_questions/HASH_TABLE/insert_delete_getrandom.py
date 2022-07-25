import random

# to do insert, remove and search in O(1), it is easy to know that we need to use a hashmap
# for getRandom, it is more tricky. Can we use python random.choice(). If we can then we dont need the array
# why do we use an array? because just by swapping an element to the front / back, we can easily remove in O(1)
# to do the swap, we require the index of the element in the array

class RandomizedSet:
    def __init__(self) -> None:
        self.my_dict = {}
        self.my_arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.my_dict:
            curr_index = len(self.my_arr)-1
            index = curr_index + 1
            self.my_arr.append(val)
            self.my_dict[val] = index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.my_dict:
            return False
        else:
            pos = self.my_dict[val]
            del self.my_dict[val]
            temp = self.my_arr[pos]
            self.my_arr[pos] = self.my_arr[0]
            self.my_arr[0] = temp
            removed = self.my_arr.pop(0)
            if removed != val:
                print("popping wrong stuff")
            return True


    def getRandom(self) -> int:
        return self.my_arr[random.randrange(0, len(self.my_arr))]


    def print_dict_arr(self):
        print(self.my_dict)
        print(self.my_arr)


if __name__ == "__main__":
    randomized_set = RandomizedSet()
    print(randomized_set.insert(5))
    print(randomized_set.insert(3))
    randomized_set.print_dict_arr()
    print(randomized_set.getRandom())
    print(randomized_set.getRandom())
    print(randomized_set.getRandom())
    print(randomized_set.remove(3))
    print(randomized_set.getRandom())
    print(randomized_set.getRandom())
    print(randomized_set.getRandom())
    randomized_set.print_dict_arr()
