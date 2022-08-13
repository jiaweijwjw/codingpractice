# https://leetcode.com/problems/container-with-most-water/

class Solution():
    def __init__(self) -> None:
        pass

    def get_max_amount_of_water(self, container):
        max_volume = 0
        left = 0
        right = len(container)-1
        while left < right and left <= len(container)-1 and right >= 0:
            height = min(container[left], container[right])
            width = right - left
            volume = height*width
            max_volume = max(max_volume, volume)
            if container[left] < container[right]:
                left += 1
            else:
                right -= 1
        return max_volume


if __name__ == "__main__":
    solution = Solution()
    inputs = [[1,8,6,2,5,4,8,3,7],[1,1]]
    # outputs: 49, 1
    for container in inputs:
        print(solution.get_max_amount_of_water(container))