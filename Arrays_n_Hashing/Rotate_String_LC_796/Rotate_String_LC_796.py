from collections import defaultdict


def concat(attributes):
    s = attributes[0]
    goal =attributes[1]

    if len(s) != len(goal):
        return False
    s_2 = s+s
    if goal in s_2:
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
        # Basic true cases
        [["abcde", "cdeab"], True],
        [["abc", "bca"], True],
        [["aaaaa", "aaaaa"], True],

        # Basic false cases
        [["abcde", "abced"], False],
        [["abc", "acb"], False], # Anagrams, but not rotations
        [["apple", "pleap"], True], # 'pleap' is  'apple' rotated

        # Different lengths
        [["abc", "abcd"], False],
        [["abcd", "abc"], False],

        # Empty strings
        [["", ""], True],

        # Single character strings
        [["a", "a"], True],
        [["a", "b"], False],

        # Longer strings
        [["abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"], True],
        [["abcdef", "fedcba"], False]
    ]

    functions = [concat]
    test(testcases, functions)
    