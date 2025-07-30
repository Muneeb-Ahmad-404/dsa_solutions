from collections import deque, defaultdict
def hashmap(nums1, nums2):

    dq = deque()
    hm = defaultdict(int)
    for curr_num in nums2:
        if not dq:
            dq.append(curr_num)
            continue
        while dq and dq[-1] < curr_num:
            hm[dq.pop()] = curr_num 
        dq.append(curr_num)
    
    while dq:
        hm[dq.pop()] = -1
    
    result = []
    for curr in nums1:
        result.append(hm[curr])

    return result       

if __name__ == '__main__':
    def test(testcases, functions):
        for i, (input_pair, expected_output) in enumerate(testcases):
            for function in functions:
                print(f"--- Running {function.__name__} ---")
                print(f'Test {i} \nInput: nums1={input_pair[0]}, nums2={input_pair[1]}') 
                result = function(input_pair[0], input_pair[1]) # Pass the list of inputs
                print(f'Expected: {expected_output} \nOutput: {result}')
                if result == expected_output:
                    print("Status: PASSED\n")
                else:
                    print("Status: FAILED\n")

    testcases = [
        # Basic examples
        [[[4,1,2], [1,3,4,2]], [-1,3,-1]],
        [[[2,4], [1,2,3,4]], [3,-1]],
        [[[1,3,5,2,4], [6,5,4,3,2,1,7]], [7,7,7,7,7]], # All have NGE from a larger list

        # No Next Greater Element
        [[[1,2,3,4], [4,3,2,1]], [-1,-1,-1,-1]],
        [[[5], [5]], [-1]],

        # Single element lists
        [[[1], [1]], [-1]],
        [[[1], [1,2]], [2]],

        # Empty lists (per problem constraints, nums1 is subset of nums2, so if nums2 is empty, nums1 must be empty too)
        [[[], []], []],
        
        # Mixed increasing/decreasing
        [[[1,5,3,6,8], [1,2,3,4,5,6,7,8,9]], [2,6,4,7,9]], 
        
        # nums1 elements at various positions in nums2
        [[[137,52,437,123], [137,52,100,200,437,123,500]], [200,100,500,500]]
    ]

    functions = [hashmap]
    test(testcases, functions)