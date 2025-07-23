from dsa_solutions.testing import test

def two_pointer(attributes):
    nums = attributes[0]

    read, write = 0, 0

    while read < len(nums):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
        read += 1

    nums[write:] = [0] * (len(nums) - write)
    return nums

def brute_force(attributes):
    nums = attributes[0]
    
    initial_length = len(nums)
    num_zeros_moved = 0
    
    i = 0
    while i < initial_length - num_zeros_moved:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            num_zeros_moved += 1
        else:
            i += 1
            
    return nums

if __name__ == '__main__':
    test_cases = [
        ([[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]),
        ([[0]], [0]),
        ([[]], []),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[0, 0, 0]], [0, 0, 0]),
        ([[5]], [5]),
        ([[0, 0]], [0, 0]),
        ([[1, 0]], [1, 0]),
        ([[0, 1]], [1, 0]),
        ([[0, 0, 1]], [1, 0, 0]),
        ([[1, 0, 0]], [1, 0, 0]),
        ([[1, 0, 2, 0, 3]], [1, 2, 3, 0, 0]),
        ([[0, 1, 2, 0, 3, 0, 4]], [1, 2, 3, 4, 0, 0, 0]),
        ([[-1, 0, 5, -2, 0, 0, 10]], [-1, 5, -2, 10, 0, 0, 0]),
        ([[1000, 0, 2000, 0, 3000, 0, 0, 0, 500]], [1000, 2000, 3000, 500, 0, 0, 0, 0, 0]),
    ]

    functions = [brute_force, two_pointer]

    test(test_cases, functions)