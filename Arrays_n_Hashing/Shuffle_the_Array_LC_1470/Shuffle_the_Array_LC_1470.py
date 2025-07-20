from dsa_solutions.testing import test

def sol(attributes):
    nums = attributes[0]
    n = attributes[1]

    result = []
    i, j = 0, n

    while i<n and j<2*n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1
    
    return result

#   return [val for i in range(n) for val in (nums[i], nums[i + n])]
if __name__ == '__main__':
   
    test_cases = [
    ([[2, 5, 1, 3, 4, 7], 3], [2, 3, 5, 4, 1, 7]),
    ([[1, 2, 3, 4, 4, 3, 2, 1], 4], [1, 4, 2, 3, 3, 2, 4, 1]),
    ([[1, 1, 2, 2], 2], [1, 2, 1, 2]),
    ([[10, 20], 1], [10, 20]),
    ([[7, 7, 7, 7], 2], [7, 7, 7, 7]),
    ([[1, 1000, 500, 10, 50, 999], 3], [1, 10, 1000, 50, 500, 999]),
    # Large array test case (n=50)
    ([[i for i in range(1, 51)] + [i for i in range(101, 151)], 50],
     [val for i in range(50) for val in (i + 1, i + 101)]),
    ]
    
    functions = [sol]
    test(test_cases, functions)