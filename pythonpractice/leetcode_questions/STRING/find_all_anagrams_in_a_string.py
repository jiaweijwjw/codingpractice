s = "cbaebabacd"
p = "abc"

class Solution():
    def __init__(self, s, p) -> None:
        self.s = s
        self.p = p

    # this question is not difficult, just make sure dont make careless mistakes in the indexes
    def find_all_anagrams(self):
        s = self.s
        p = self.p
        ans = []
        if len(p) > len(s): # if s is shorter than p, it definitely cannot be an anagram already
            return ans
        # dictionary of the count of chars in string p, used for comparison / read only
        p_dict = {}
        for char in p:
            p_dict[char] = p_dict.get(char, 0) + 1 # shortcut way of using dict to count
        # start and end for window
        s_dict = {}
        start = 0
        end = len(p)-1
        # initially have to populate all the chars in the window into s_dict
        for i in range(start, end+1):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        if s_dict == p_dict: # before sliding, check whether there is any anagram for the window initializing (filling up s_dict with initial window)
            ans.append(start)
        while end < len(s)-1: # when end of window reaches the last char in string s
            # remove the front element from s_dict
            if s_dict[s[start]] == 1:
                del s_dict[s[start]]
            else:
                s_dict[s[start]] -= 1
            # add the back element to s_dict
            s_dict[s[end+1]] = s_dict.get(s[end+1], 0) + 1
            # shift the window
            start += 1
            end += 1
            if s_dict == p_dict:
                ans.append(start) # append only after shifting the window
        return ans

    
if __name__ == "__main__":
    solution = Solution(s, p)
    print(solution.find_all_anagrams())
