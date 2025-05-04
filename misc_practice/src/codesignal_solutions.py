'''
Solutions for https://codesignal.com/blog/interview-prep/key-python-interview-questions-and-answers-from-basic-to-senior-level/#basic
'''

def get_math(nums: list):

    add = 0
    highest = nums[0]

    for num in nums:
        if type(num) != float or type(num) != int:
            continue

        add = add + num

        if num > highest:
            highest = num

    return add, highest

def get_count(nums: list,
              element):

    count = 0

    for num in nums:

        if num == element:

            count += 1
    return count

def reverse_string(string: str) -> str:

    # hello --> 4 3 2 1 0
    result = ''
    length = len(string)

    for i in range(length-1, -1, -1):

        result += string[i]

    return result, result == string


def get_palindromes(string: str) -> list:

    result = []

    # radar --> r, a, d, radar, ada
    # start with first char, then iterate over all others and check for palindrome

    length = len(string)
    # iterate over the starting char
    for i in range(length):

        for si in range(i+1, length):
            if si > (length-1):
                break

            substring = string[i:si]

            if substring == substring[::-1] and substring not in result:
                result.append(substring)

    return result
