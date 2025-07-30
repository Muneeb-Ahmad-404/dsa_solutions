from collections import defaultdict
def hash(nums):
    dict = defaultdict(int)
    for num in nums:
        dict[num] = 1
    
    for i in range(0, len(nums)+1):
        if dict[i] == 0:
            return i
    return -1

def sum_solution(nums):
    
    return sum(range(0,len(nums)+1)) - sum(nums)
    
def xor(nums):
    missing = len(nums)

    for i in range(0, len(nums)):
        missing = missing ^ i ^ nums[i]
    return missing


def run_tests(test_cases, functions_to_test):
    for i, (input_data, expected_output) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Input: {input_data}")
        
        for func in functions_to_test:
            print(f"Running function: {func.__name__}")
            actual_output = func(input_data)
            
            print(f"Expected: {expected_output}")
            print(f"Actual: {actual_output}")

            if actual_output == expected_output:
                print("Status: PASSED\n")
            else:
                print("Status: FAILED\n")


if __name__ == '__main__':
    testcases = [
    [[3, 0, 1], 2],
    [[0, 1], 2],
    [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
    [[1, 2, 3], 0],
    [[1], 0],
    [[0, 1, 2], 3],
    [[0], 1],
    [[0, 2, 3, 1, 5], 4],
    [[0, 2], 1],
    [[], 0],
    ] 
    functions_to_test = [hash, sum_solution, xor]
    run_tests(testcases, functions_to_test)