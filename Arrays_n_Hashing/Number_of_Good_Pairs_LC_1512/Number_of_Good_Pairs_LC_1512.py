import math
from dsa_solutions.testing import test
from collections import defaultdict

def brute_force(attributes):
    nums = attributes[0]

    groups = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                groups += 1
    return groups

def hash_approach(attributes):
    nums = attributes[0]

    hash = defaultdict(int)
    for num in nums:
        hash[num] += 1

    groups = 0
    for key in hash:
        value = hash[key]
        if value > 1:
            groups += sum(range(value))
    return groups

if __name__ == '__main__':
    test_cases = [
    ([[1, 2, 3, 1, 1, 3]], 4),
    ([[1, 1, 1, 1]], 6),
    ([[1, 2, 3]], 0),
    ([[1, 2, 3, 1]], 1),
    ([[7]], 0),
    ([[1, 100, 1, 100, 50]], 2),
    ([[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7]], 7),
    ]

    functions = [brute_force, hash_approach]

    test(test_cases, functions)