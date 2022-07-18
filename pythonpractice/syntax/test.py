
def main():
    N = input()
    nums_string = input()
    nums_string_list = nums_string.split()
    nums = [int(num) for num in nums_string_list]
    return check_repeated(nums)

def check_repeated(nums):
    checked = set()
    for num in nums:
        if num in checked:
            return "happy"
        else:
            checked.add(num)
    return "sad"

if __name__ == "__main__":
    print(main())


