import itertools
from dsa_solutions.testing import test

def loop(attributes):
    nums = attributes[0]

    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    print(nums)
    return nums

def rec(attributes):
    nums = attributes[0]
    help_rec(nums, len(nums)-1)

#theres a problem with it will deal later
def help_rec(nums, n):
    if n <=0:
        return 0
    if n == 0:
        return nums[n]
    nums[n] += help_rec(nums, n-1)
    if n == len(nums)-1: return nums
    return nums[n]


def iter_tools(attributes):
    nums = attributes[0]

    return list(itertools.accumulate(nums))


if __name__ == '__main__':

    test_cases = [
        ([[]], []),
        ([[0, 0, 0, 0]], [0, 0, 0, 0]),
        # ([[1] * 500], list(range(1, 501))),
        ([[-1, -2, -3, -4]], [-1, -3, -6, -10]),
    ]

    functions = [loop, iter_tools, rec]

    test(test_cases, functions)

