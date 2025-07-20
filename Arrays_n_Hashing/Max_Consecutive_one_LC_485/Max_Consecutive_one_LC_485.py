from dsa_solutions.testing import test

def solution(attributes):
    nums = attributes[0]

    max_count = 0
    temp_count = 0

    for num in nums:
        if num == 1: 
            temp_count += 1
        else:
            max_count = max(max_count, temp_count)
            temp_count = 0
    max_count = max(max_count, temp_count)
    return max_count

if __name__ == '__main__':
    test_cases = [
        ([[1, 1, 0, 1, 1, 1]], 3),
        ([[1, 0, 1, 1, 0, 1]], 2),
        ([[]], 0),
        ([[1]], 1),
        ([[0]], 0),
        ([[1, 1, 1, 1, 1]], 5),
        ([[0, 0, 0, 0]], 0),
        ([[1, 0, 0, 0]], 1),
        ([[0, 0, 0, 1]], 1),
        ([[0, 1, 0]], 1),
        ([[1, 0]], 1),
        ([[0, 1]], 1),
        ([[0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1]], 4),
        ([[1, 0, 1, 0, 1, 0, 1]], 1),
        ([[0, 0, 0, 1, 1, 1, 0, 1, 1, 0]], 3),
        ([[1, 1, 0, 0, 1, 1]], 2),
        ([[0, 1, 1, 1, 1, 1, 0]], 5),
        ([[1, 1, 1, 1, 0, 1, 1, 1, 1, 1]], 5),
    ]

    functions = [solution]
    test(test_cases, functions)
            