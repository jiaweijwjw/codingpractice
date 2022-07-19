def main():
    N = input() # read the first line
    nums_string = input() # read the second line, will be a string
    nums_string_list = nums_string.split() # split the string by whitespaces, will return a list. so from "1 2 3 4" becomes ["1", "2", "3", "4"]
    nums = [int(num) for num in nums_string_list] # change everything to an int. not necessary for this question. using list comprehension can google this, useful
    return check_repeated(nums)

def check_repeated(nums):
    checked = set() # use a set or dict to check for existence of something. go read up the data structure if you dk how it works
    # since we not need to store any values, we can just use a set instead of a dict
    for num in nums: # iterate through all the numbers in the array
        if num in checked: # if the number is already in the set, we can exit early by returning "happy"
            return "happy"
        else: # if the number is not in the set, add it to the set
            checked.add(num)
    return "sad" # at the end, after you iterate through everything and there is no early exit, means that no numbers are repeated. so we return "sad"

if __name__ == "__main__": # this just means run the following code if you do run "python filename.py" in the command line.
    # if you import the above functions from this file in another file, this part wont run. can google for more details
    print(main())
