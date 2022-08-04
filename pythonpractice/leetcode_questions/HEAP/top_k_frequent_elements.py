from heapq import heappush, nlargest

class Solution():
    def __init__(self) -> None:
        pass

    def get_top_f_frequent_elements(self, nums, k):
        heap = []
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        for key, value in count_dict.items(): # key is the num, value is the count
            heappush(heap, (value, key)) # store value as first element in tuple so the heap sorting will be easier
        return [item[1] for item in nlargest(k, heap)]


if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(solution.get_top_f_frequent_elements(nums, k))