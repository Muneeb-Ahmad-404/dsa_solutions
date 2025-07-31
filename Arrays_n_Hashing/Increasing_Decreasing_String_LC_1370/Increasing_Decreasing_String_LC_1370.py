import string
from collections import defaultdict
def hash(s):
    dict = defaultdict(int)
    for char in s:
        dict[char] += 1
    result = ''
    alphabets = list(string.ascii_lowercase)
    i = 0
    while i < len(s):
        for alphabet in alphabets:
            if dict[alphabet] != 0:
                result += alphabet
                dict[alphabet] -= 1
                i += 1
        for alphabet in reversed(alphabets):
            if dict[alphabet] != 0:
                result += alphabet
                dict[alphabet] -= 1
                i += 1
    return result

testcases = [
    ["aaaabbbbcccc", "abccbaabccba"],
    ["rat", "art"],
    ["leetcode", "cdelotee"],
    ["aabcc", "abcca"],
    ["a", "a"],
    ["ab", "ab"],
    ["ba", "ab"],
    ["acb", "abc"],
    ["bbbb", "bbbb"],
    ["zbca", "abcz"],
    ["yza", "ayz"],
    ["", ""]
]

def run_tests(test_cases, functions_to_test):
    for i, (input_string, expected_output) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Input: '{input_string}'")

        for func in functions_to_test:
            print(f"Running function: {func.__name__}")
            actual_output = func(input_string)

            print(f"Expected: '{expected_output}'")
            print(f"Actual:   '{actual_output}'")

            if actual_output == expected_output:
                print("Status: PASSED\n")
            else:
                print("Status: FAILED\n")

if __name__ == '__main__':
    functions_to_test = [hash]
    run_tests(testcases, functions_to_test)