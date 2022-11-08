# https://leetcode.com/problems/first-bad-version/

class Solution():
    def __init__(self, bad) -> None:
        self.bad = bad

    def is_bad_version(self, version):
        return version >= self.bad

    def get_first_bad_version(self, n):
        def binary_search(start, end, mid):
            if start > end:
                return -1
            # if mid == 1 or mid == n: # since guaranteed that there is a bad version. this will fail (2,2) edge case
            #     return mid
            if (mid == 1 or mid == n) and self.is_bad_version(mid):
                return mid
            elif not self.is_bad_version(mid-1) and self.is_bad_version(mid+1): # first bad is found anywhere else
                if self.is_bad_version(mid): # have to check mid is bad also, if not can get last good version also
                    return mid
                else:
                    return mid+1
            elif self.is_bad_version(mid-1) and self.is_bad_version(mid+1): # search left. it wont be 'out of bounds' as we already checked in first condition mid is not first and last element
                end = mid-1
                mid = (start+end)//2
                return binary_search(start, end, mid)
            elif not self.is_bad_version(mid-1) and not self.is_bad_version(mid+1): # search right
                start = mid+1
                mid = (start+end)//2
                return binary_search(start, end, mid)
        return binary_search(1, n, (n+1)//2)

    # the above version is easy to understand, just more edge cases. but notice that while checking the values,
    # we are checking left and right. is there a way that we can reduce this to just checking the mid value?
    # then we can halve the current number of API calls to is_bad_version()

    # we can do this but using iterative binary search instead.
    # instead of using the mid variable to find the answer, we are reducing the search space and then returning the left boundary of the search space
    # be careful with the condition checking as the edges are very important for binary search
    # bascially what we are trying to do is to shift the start pointer to point to the first bad version

    # for iterative binary search,
    # when to exit the loop?
    # how to update the boundary?
    def get_first_bad_version2(self, n):
        def binary_search(start, end, mid):
            while start < end: # cannot include the equality case
                mid = (start+end)//2
                if not self.is_bad_version(mid):
                    start = mid+1 # dont include mid as mid is good version. rmb that start is to keep track of the first bad
                else:
                    end = mid # include mid as mid is bad version, you never know if this is the first bad, so dont exceed
            return start
        return binary_search(1, n, (n+1)//2)



if __name__ == "__main__":
    inputs = [(5,4),(1,1),(2,2)]
    # outputs: 4, 1, 2
    for n, bad in inputs:
        solution = Solution(bad)
        print(solution.get_first_bad_version(n))
        print(solution.get_first_bad_version2(n))

# this is quite similar to the tiktok live round2 binary search question
# what are the edge cases? 
# 1. the first bad is the first version
# 2. the first bad is the last version
# note that a bad version exists (constraints of the question). makes it easier
# for case1, when mid is the left most element in the array and the right is a bad version
# for case2, when mid is the right most element in the array and left is a good version
# when is the 'hit' cases? when the left of mid is a good version and the right of mid is a bad version
# when to search left? when left and right of mid is bad
# when to search right? when left and right of mid is good