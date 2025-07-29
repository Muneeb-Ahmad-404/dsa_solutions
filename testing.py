def test(testcases, functions):
    for i in range(len(testcases)):
        for function in functions:
            print(f"--- Running {function.__name__} ---")
            print(f'Test {i} \nInput: {testcases[i][0]}') 
            result = function(testcases[i][0])
            print(f'Expected: {testcases[i][1]} \nOutput: {result}')
            if result == testcases[i][1]:
                print("Status: PASSED\n")
            else:
                print("Status: FAILED\n")
