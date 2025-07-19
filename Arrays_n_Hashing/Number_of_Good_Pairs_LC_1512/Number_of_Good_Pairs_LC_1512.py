import math
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


print(brute_force([[1,2,3,4,1,5,1,2,3,3,1,1]]))
print(hash_approach([[1,2,3,4,1,5,1,2,3,3,1,1]]))