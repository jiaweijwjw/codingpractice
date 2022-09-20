class Solution():
    def __init__(self) -> None:
        pass

        # the idea is very simple, the decision tree is just whether we add a particular element or not. do this for every element in the array
    def get_all_subsequences_min_size_k(self, arr, k):
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
    inputs = [[1,2,3]]
    for arr in inputs:
        print(solution.get_all_subsequences_min_size_k(arr, 2))