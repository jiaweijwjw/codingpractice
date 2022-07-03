class Solution():
    def __init__(self) -> None:
        self.storage = set()

    def store(self, num: int) -> None:
        """Adds an integer to the store"""
        # if we use set() as storage, we dont even need to check this: if num not in self.storage:
        self.storage.add(num)

    def has_two_addends_summing_to(self, value: int) -> bool:
        """Returns True if any pair of numbers in the store add up to the given value"""
        checked = set()
        for num in self.storage:
            rem = value - num
            if rem in checked:
                return True
            else:
                checked.add(num)
        return False

# If you run the module directly, execute the function, if you import the module, don’t run it.
if __name__ == "__main__":
    some_list = [2,5,3,2]
    test_value = 4
    solution = Solution()
    for num in some_list:
        solution.store(num)
    print(solution.has_two_addends_summing_to(test_value))