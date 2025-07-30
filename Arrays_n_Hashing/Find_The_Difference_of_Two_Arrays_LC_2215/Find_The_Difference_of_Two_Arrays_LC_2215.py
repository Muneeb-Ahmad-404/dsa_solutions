from collections import defaultdict
def set_solution(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set1-set2), list(set2-set1)]

def run_tests(test_cases, functions_to_test):
    print("\n--- Starting Test Suite ---")
    for i, (input_data, expected_output) in enumerate(test_cases):
        print(f"\nTest Case {i+1}:")
        print(f"Input: nums1={input_data[0]}, nums2={input_data[1]}")        
        for func in functions_to_test:
            print(f"  Running function: {func.__name__}")
            
            actual_output = func(input_data[0], input_data[1]) 
            
            expected_set_0 = set(expected_output[0])
            expected_set_1 = set(expected_output[1])
            actual_set_0 = set(actual_output[0])
            actual_set_1 = set(actual_output[1])

            if (actual_set_0 == expected_set_0) and \
               (actual_set_1 == expected_set_1):
                print(f"  Result: PASSED")
                print(f"  Output: {actual_output}")
            else:
                print(f"  Result: FAILED")
                print(f"  Expected: {expected_output}")
                print(f"  Actual: {actual_output}")
    print("\n--- Test Suite Finished ---")



if __name__ == '__main__':
    test_cases = [
    [[[], []], [[], []]],
    [[[1], [2]], [[1], [2]]],
    [[[1], [1]], [[], []]],
    [[[1, 2], [2, 3]], [[1], [3]]],
    [[[10, 20], [20, 10]], [[], []]], 
    [[[1, 2, 3], []], [[1, 2, 3], []]],
    [[[], [4, 5, 6]], [[], [4, 5, 6]]],
    [[[1, 2, 2, 3], [2, 3, 3, 4]], [[1], [4]]],
    [[[5, 5, 6, 7], [6, 8, 8, 9]], [[5, 7], [8, 9]]],
    [[[1,1,1], [1,1,1]], [[],[]]], 
    [[[1, 3, 5], [2, 4, 6]], [[1, 3, 5], [2, 4, 6]]], 
    [[[1, 2, 3], [2, 3, 4]], [[1], [4]]],             
    [[[7, 8, 9], [9, 7, 8]], [[], []]],             
    [[[1, 2, 3], [3, 1, 2]], [[], []]],
    [[[1, 1, 2, 3], [3, 2, 1]], [[], []]], 

    [[[i for i in range(10)], [i for i in range(5, 15)]], [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14]]],
    [[[100,200,300,400], [200,400,500,600]], [[100,300], [500,600]]],
]
    functions = [set_solution]
    
    run_tests(test_cases, functions)