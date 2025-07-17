def test(testcases, functions):
    for i in range(len(testcases)):
        for function in functions:
            print(function.__name__)
            result = function(testcases[i][0])
            print(f'Test {i}  \nExpected: {testcases[i][1]} \nOutput: {result}')