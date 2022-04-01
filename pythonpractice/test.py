list_of_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list_of_nums2 = [9, 10, 11, 12]
string_helloworld = "helloworld"

list_of_nums_str = list(map(str, list_of_nums))
print(list_of_nums_str)

set_helloworld = {char for char in string_helloworld}
print(set_helloworld)

string_helloworld2 = "".join(filter(lambda char: True if char in ["a", "e", "i", "o", "u"] else False, string_helloworld))
print(string_helloworld2)

val1, val2, val3, val4 = -66.6, -66.5, -66.4, -66.4321
print(abs(round(val4, 2))) # 66.43

def forloop1(string_helloworld):
    string_result = ""
    for i in string_helloworld: # each char
        #string_result.join(i) # join(iterator)
        string_result += i
    return string_result

def forloop2(string_helloworld):
    string_result = ""
    for i in range(len(string_helloworld)): # index of each char
        string_result += string_helloworld[i]
    return string_result

def forloop3(string_helloworld):
    string_result = ""
    for i in range(len(string_helloworld)-1, -1, -1):
        string_result += string_helloworld[i]
    return string_result

def forloop4(string_helloworld):
    string_result = ""
    for i in range(0, len(string_helloworld)):
        string_result += string_helloworld[i]
    return string_result

def forloop5(string_helloworld):
    string_result = ""
    string_result2 = ""
    for i, char in enumerate(string_helloworld):
        string_result += char
        string_result2 += string_helloworld[i]
    return string_result, string_result2

# for and while loop can have optional else block

print(forloop1(string_helloworld))
print(forloop2(string_helloworld))
print(forloop3(string_helloworld))
print(forloop4(string_helloworld))
print(forloop5(string_helloworld))
print("".join([char for char in string_helloworld]))

newstring = string_helloworld.center(len(string_helloworld)+3, "*")
print(newstring)
print(string_helloworld.upper())