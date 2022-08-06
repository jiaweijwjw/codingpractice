class Solution():
    def __init__(self) -> None:
        pass

    def multiply_strings(self, s1, s2):
        ans_arr = [0]*(len(s1)*len(s2))
        for i in range(len(s2)-1, -1, -1):
            carry = 0
            for j in range(len(s1)-1, -1, -1):
                prod = int(s2[i]) * int(s1[j]) + carry
                carry = prod // 10
                rem = prod % 10
                ans_arr[j-((len(s2)-1)-1)] += rem
                if j == 0 and carry > 0:
                    ans_arr[]
        ans = "".join(map(str, ans_arr)).lstrip('0')
        return ans

if __name__ == "__main__":
    solution = Solution()
    s1, s2 = "123", "456"
    print(solution.multiply_strings(s1, s2))