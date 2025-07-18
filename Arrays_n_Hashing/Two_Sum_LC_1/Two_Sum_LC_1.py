from dsa_solutions.testing import test
from collections import defaultdict 

def brute_force(attributes):
    nums = attributes[0]
    target = attributes[1]

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target: return [i, j]
    return []

def hash_map(attributes):
    nums = attributes[0]
    target = attributes[1]

    hash = defaultdict(list)

    for idx, value in enumerate(nums):
        hash[value].append(idx)
    
    for value in hash:
        other = target - value
        sol = []
        if hash.get(other) != None:
            if hash[other] == hash[value]:
                if len(hash[value]) > 1:
                    sol = [hash[value][0], hash[value][1]]
                    break
                else:
                    continue
            sol = [hash[value][0], hash[other][0]]
            break
    return sol

def hash_map_twoway_NC(attributes):
    nums = attributes[0]
    target = attributes[1]

    indices = {}

    for i, n in enumerate(nums):
        indices[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]
   

def hash_map_oneway_NC(attributes):
    nums = attributes[0]
    target = attributes[1]
    prev_map = {}

    for idx, value in enumerate(nums):
        other = target - value
        if other in prev_map:
            return [other, idx]
        prev_map[idx] = value


if __name__ == '__main__':
    test_cases = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([1, 2, 3, 4, 5, 6], 7), [0, 5]), #these test cases are not right for the one_way solution if
    (([10, 2, 8, 5], 10), [1, 2]),          #multiple solutions exist
    (([3, 3], 6), [0, 1]),
    (([1, 2, 2, 3], 4), [0, 3]),
    (([4, 5], 9), [0, 1]),
    (([1, 2, 3, 4], 10), []),
    (([5, 5], 11), []),
    (([1, 2, 3], 7), []),
    (([-1, -2, -3, -4], -3), [0, 1]),
    (([-1, 2, 5, 7], 4), [0, 2]),
    (([1, -5, 10, -2], -7), [1, 3]),
]

    functions = [brute_force, hash_map, hash_map_twoway_NC, hash_map_oneway_NC]
    test(test_cases, functions)
