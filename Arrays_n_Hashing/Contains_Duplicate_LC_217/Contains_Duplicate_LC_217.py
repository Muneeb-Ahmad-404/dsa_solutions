from testing import test

def bruteforce(nums):
    has_duplicate = False
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                has_duplicate = True
                break
    return has_duplicate


def set_approach1(nums):
    return (len(set(nums)) != len(nums))

def set_approach2(nums):
    unique_set = set()
    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)
    return False

def hash_approach(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            return True
        hashmap[num] = 1
    return False

if __name__ == '__main__':
    test_cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([], False),
        ([7], False),
        ([1,1,1,1,1], True),
        (list(range(1000)), False),
        ([i % 10 for i in range(1000)], True)
    ]

    functions = [bruteforce, set_approach1, set_approach2, hash_approach]

    my_tester = testing()
    my_tester.test(test_cases, functions)
        
