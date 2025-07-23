from dsa_solutions.testing import test
def brute_force(attributes):
    nums = attributes[0]
    k = attributes[1]

    n = len(nums)

    if n == 0 or k == 0: 
        return nums

    k = k % n

    for _ in range(k):
        last = nums[n - 1]
        for j in range(n - 2, -1, -1):
            nums[j + 1] = nums[j]
        nums[0] = last
        
    return nums

def three_reverse_solution(attributes):
    nums = attributes[0]
    k = attributes[1]

    n = len(nums)

    if n == 0 or k == 0:
        return nums

    k = k % n

    def reverse_segment(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse_segment(nums, 0, n - 1)

    reverse_segment(nums, 0, k - 1)

    reverse_segment(nums, k, n - 1)
    
    return nums

            


if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3, 4, 5, 6, 7], 3], [5, 6, 7, 1, 2, 3, 4]),
        ([[-1, -100, 3, 99], 2], [3, 99, -1, -100]),
        ([[], 0], []),
        ([[], 5], []),
        ([[1], 0], [1]),
        ([[1], 1], [1]),
        ([[1], 5], [1]),
        ([[1, 2, 3, 4], 0], [1, 2, 3, 4]),
        ([[1, 2, 3, 4], 4], [1, 2, 3, 4]),
        ([[1, 2, 3], 6], [1, 2, 3]),
        ([[1, 2, 3, 4, 5], 1], [5, 1, 2, 3, 4]),
        ([[1, 2, 3, 4, 5], 4], [2, 3, 4, 5, 1]),
        ([[1, 2, 3, 4, 5], 2], [4, 5, 1, 2, 3]),
        ([[1, 2, 3], 4], [3, 1, 2]),
        ([[1, 2], 5], [2, 1]),
        ([[1, 2, 3, 4, 5, 6], 2], [5, 6, 1, 2, 3, 4]),
        ([[10, 20, 30, 40, 50], 3], [30, 40, 50, 10, 20]),
        ([[-5, -10, -15, -20], 1], [-20, -5, -10, -15]),
        ([[1, 1, 2, 2, 3, 3], 2], [3, 3, 1, 1, 2, 2]),
    ]

    functions = [three_reverse_solution]
    test(test_cases, functions)


#as the solutions are inplace only one function can be used correctly as for the second one the list would
#have already been changed
