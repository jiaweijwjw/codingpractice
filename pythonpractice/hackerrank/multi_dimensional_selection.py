from math import inf
import itertools

class Solution():
    def __init__(self) -> None:
        pass

    def get_max_product(self, arr):
        num_rows = len(arr)
        num_cols = len(arr[0])
        subsequences = []
        for row in arr:
            subsequences.append(self.get_all_subsequences(row, len(row)//2))
        print(subsequences)
        selections = set()
        # all combinations vs cartesian product: cartesian product can have duplicates
        min_diff = inf
        for cartesian_prod in itertools.product(*subsequences):
            item = list(itertools.chain(*(i if isinstance(i, list) else (i,) for i in cartesian_prod)))
            min_val = min(item)
            max_val = max(item)
            diff = abs(max_val-min_val)
            if diff < min_diff:
                selections = [item]
            elif diff == min_diff:
                selections.append(item)
            min_diff = min(min_diff, diff)
        print(selections)
        print(min_diff)
        lengths = list(map(len, selections))
        print(lengths)
        return min_diff*max(lengths)

    def get_all_subsequences(self, arr, k):
        ans = []
        def recursive(index=0, subarray=[]):
            nonlocal ans
            if index == len(arr):
                if len(subarray) >= k:
                    ans.append(subarray)
                return
            recursive(index=index+1, subarray=subarray+[arr[index]]) # include 
            recursive(index=index+1, subarray=subarray) # dont include
        recursive()
        return ans

if __name__ == "__main__":
    solution = Solution()
    arr = [[1,2],[3,4],[8,9]]
    print(solution.get_max_product(arr))

    # min_diff = inf
    # for tups in itertools.product(*arr):
    #     item = list(itertools.chain(*(i if isinstance(i, list) else (i,) for i in tups)))
    #     print(item)
    #         # print(el)
    #         # min_val = min(el)
    #         # max_val = max(el)
    #         # diff = abs(max_val-min_val)
    #         # print(diff)
