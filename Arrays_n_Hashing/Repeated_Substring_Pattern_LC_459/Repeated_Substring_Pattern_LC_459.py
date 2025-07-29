
def solution(attributes):
    s = attributes[0]
    n = len(s)

    if n <= 1:
        return False

    for L in range(1, n // 2 + 1):
        if n % L == 0:
            potential_pattern = s[0:L]
            num_repetitions = n // L
            if potential_pattern * num_repetitions == s:
                return True
                
    return False

if __name__ == '__main__':
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

    testcases = [
    [["abab"], True],
    [["abcabc"], True],
    [["ababab"], True],
    [["aaaa"], True],
    [["abcabcabcabc"], True],
    [["abc"], False],
    [["aba"], False],
    [["a"], False],
    [["abac"], False],
    [["abcdefgh"], False],
    [[""], False],
    [["a"], False],
    [["aa"], True],
    [["abacaba"], False],
    [["zzza"], False],
    [["abcdeabcde"], True],
    [["abracadabra"], False]
    ]

    functions = [solution]
    test(testcases, functions)