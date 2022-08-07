class Solution():
    def __init__(self) -> None:
        pass

    # the purpose of this question is to solve the multiplication of 2 very large numbers that cannot fit into our integer type
    # the algorithm to do the multiplication would be the same as how you would do it on paper. try to write it out first to get the general idea
    # notice that the len of the largest answer would be the len of string1 + string 2. for example, 99x999=98901, 99x99=9801
    # we then initialize the ans array to be zeroes first. each of the element in this list would correspond to an integer 1 to 9 at the respective position
    # we then loop through the 2 strings from the back to do the multiplication.
    # one way to do it could be to reverse the string first, then start from the front. 
    # the reason is because we want to maintain the 0 based index even though we are iterating from the back
    # however, list splicing / reversing in python incurs O(n) time
    # the way i decided to do it is to use a normal for loop iterating from the back while maintaining 2 pointers, shift_pos and pos
    # pos is exactly the position of the number in the inner loop which we are currently multiplying
    # shift pos is the shift needed when multiplying the number in the outer loop. this is exactly the same as when doing the multiplication by hand
    # since every multiplication we are doing is a 1 digit x 1 digit multiplication, we just need to handle the ones and tens as max is a 2 digit number
    # we will first add the ones value to what is currently already in the ones position in the answer array
    # if there is any overflow (>= 10), we need to bring it over to the tens position for this iteration
    # we dont have to check for overflow in the tens position in this iteration as it will be handled in the next iteration.
    # the ones position in an iteration is the tens position in the previous iteration. hence if there was an overflow, it will be corrected
    # the time complexity is O(nm) where n is the length of string1 and m is the length of string2
    # the space complexity would be O(n+m) to store the answer array
    def multiply_strings(self, s1, s2):
        ans_arr = [0]*(len(s1)+len(s2))
        shift_pos = 0
        for i in range(len(s2)-1, -1, -1):
            pos = 0
            for j in range(len(s1)-1, -1, -1):
                ones_position = len(ans_arr)-1-shift_pos-pos # we can use this trick if we use 0 base index but loop from backwards
                prod = int(s2[i]) * int(s1[j])
                ones = prod % 10
                tens = prod // 10
                ans_arr[ones_position] += ones
                if ans_arr[ones_position] > 9:
                    carry = ans_arr[ones_position] // 10 # have to store the value of carry before it is modified. dont make the careless mistake
                    ans_arr[ones_position] = ans_arr[ones_position] % 10
                    ans_arr[ones_position-1] += carry
                ans_arr[ones_position-1] += tens
                # we dont have to account for this if we think in this way:
                # every position will be accounted for when we move on to the next iteration
                # also, the last one confirm wont overflow since we already know 99x99 only maximum 9801, notice the 9 wont be exceeded
                # if j == 0 and ans_arr[ones_position-1] > 9:
                #     carry = ans+arr[ones_position-1] // 10 
                #     ans_arr[ones_position-1] = ans_arr[ones_position-1] % 10
                #     ans_arr[ones_position-2] += carry
                pos += 1
            shift_pos += 1
        ans = "".join(map(str, ans_arr)).lstrip('0')
        return ans or "0" # empty strings are False

if __name__ == "__main__":
    solution = Solution()
    s1, s2 = "123456789", "987654321"
    print(solution.multiply_strings(s1, s2))