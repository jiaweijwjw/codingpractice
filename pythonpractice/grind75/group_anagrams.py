# https://leetcode.com/problems/group-anagrams/

class Solution():
    def __init__(self) -> None:
        pass

    def group_anagrams2(self, strings):
        ans = []
        dict_of_sets = {} # key is the set, value is list of actual strings
        for string in strings:
            chars = {} # we need to store count as anagram can make up of same letters but different count frequencies
            for char in string:
                chars[char] = chars.get(char, 0) + 1
            characters = tuple(sorted(chars.items())) # to freeze a dict
            if characters in dict_of_sets:
                dict_of_sets[characters].append(string)
            else:
                dict_of_sets[characters] = [string]
        for key, value in dict_of_sets.items():
            ans.append(value)
        return ans

    # faster way
    def group_anagrams(self, strings):
        my_dict = {}
        for string in strings:
            sorted_string = "".join(map(str, sorted(string)))
            my_dict[sorted_string] = my_dict.get(sorted_string, []) + [string]
        return list(my_dict.values())

if __name__ == "__main__":
    solution = Solution()
    inputs = [["eat","tea","tan","ate","nat","bat"],[""],["a"]]
    # outputs: [["bat"],["nat","tan"],["ate","eat","tea"]], [[""]], [["a"]]
    for strings in inputs:
        print(solution.group_anagrams(strings))