from dsa_solutions.testing import test

def smart(attributes):
    nums = attributes[0]
    return nums * 2 #or nums + nums

def brute_force(attributes):
    nums = attributes[0]

    n  = len(nums)
    result = [0] * n * 2
    for i in range(n):
        result [i], result[i + n] = nums[i], nums[i]
    return result


if __name__ == '__main__':
    test_cases = [
    ([[1, 2, 1]], [1, 2, 1, 1, 2, 1]),
    ([[5]], [5, 5]),
    ([[-1, -2]], [-1, -2, -1, -2]),
    ([[0, 0, 0]], [0, 0, 0, 0, 0, 0]),
    ([[10, -5, 0]], [10, -5, 0, 10, -5, 0]),
    ([[i for i in range(100)]], [i for i in range(100)] + [i for i in range(100)]),
    ]

    functions = [brute_force, smart]

    test(test_cases, functions)   