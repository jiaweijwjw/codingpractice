class Solution():
    def __init__(self) -> None:
        pass

    def get_all_subarrays_iterative(self, arr):
        ans = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                ans.append(arr[i:j+1]) # +1 is to include
        return ans

    def get_all_subarrays_min_size_k_iterative(self, arr, k):
        ans = []
        for i in range(len(arr)-k):
            for j in range(i+k-1, len(arr)):
                ans.append(arr[i:j+1]) # +1 is to include
        return ans

    def get_all_subarrays_size_k_sliding_window(self, arr, k):
        ans = []
        start = 0
        end = start + k - 1
        if len(arr) < k:
            return ans
        while end < len(arr):
            ans.append(arr[start:end+1])
            start += 1
            end += 1
        return ans
        

if __name__ == "__main__":
    solution = Solution()
    inputs = [[1,2,3,4]]
    for arr in inputs:
        print(solution.get_all_subarrays_iterative(arr))
        print(solution.get_all_subarrays_min_size_k_iterative(arr, 2))
        print(solution.get_all_subarrays_size_k_sliding_window(arr, 2))