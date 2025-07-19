from dsa_solutions.testing import test
import math

def brute_force(attributes):
    nums = attributes[0]

    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    
    nums.sort()
    return nums

def two_pointer(attributes):
    nums = attributes[0]

    result = [0] * len(nums)
    i = 0
    j = len(nums) - 1
    k = j

    while i<=j:
        i_squared = nums[i] * nums[i]
        j_squared = nums[j] * nums[j]

        if k < 0: return

        if i_squared > j_squared:
            i += 1
            result[k] = i_squared
            k -= 1
        else:
            j -= 1
            result[k] = j_squared
            k -= 1

    return result


if __name__ == '__main__':
    test_cases = [
        ([[]], []),
        ([[-4, -2, -1]], [1, 4, 16]),
        ([[-100, -99, -50, 0, 1, 50, 99]], [0, 1, 2500, 2500, 9801, 9801, 10000]), # More complex mix for large array check
        ([[x for x in range(-100, 100)]], sorted([x**2 for x in range(-100, 100)])),
    ]

    functions = [brute_force, two_pointer]

    test(test_cases, functions)
