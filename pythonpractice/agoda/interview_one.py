class Solution():
    def __init__(self) -> None:
        self.storage = set()

    def store(self, num: int) -> None:
        """Adds an integer to the store"""
        if num not in self.storage:
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


some_list = [2,5]
test_value = 4
solution = Solution()
for num in some_list:
    solution.store(num)
print(solution.has_two_addends_summing_to(test_value))