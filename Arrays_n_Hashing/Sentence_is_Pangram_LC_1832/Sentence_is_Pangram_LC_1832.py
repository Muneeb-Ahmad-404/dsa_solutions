from collections import defaultdict
def set_solution(sentence):
    map = set()#the edge cases delt here are not present in the leet code problem
    #you can go without using the if .isalpha and .lower part of the code too
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            map.add(char)
    return len(map) == 26

def hash_solution(sentence):
    hash = defaultdict(int)
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            hash[char] = 1
    return len(hash) == 26

testcases = [
    ["thequickbrownfoxjumpsoverthelazydog", True],
    ["leetcode", False],
    ["abcdefghijklmnopqrstuvwxy", False],
    ["this is not a pangram", False],
    ["a quick brown fox jumps over the lazy dog", True],
    ["", False],
    ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", True],
    ["abcdefghij-k lmnopqrstuv wxyz", True],
    ["1234567890", False],
    ["abcdefghijklmnopqrstuvwxyza", True]
]

def run_tests(test_cases, functions_to_test):
    for i, (sentence, expected_output) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Sentence: '{sentence}'")
        
        for func in functions_to_test:
            print(f"Running function: {func.__name__}")
            actual_output = func(sentence)

            print(f"Expected: {expected_output}")
            print(f"Actual: {actual_output}")

            if actual_output == expected_output:
                print("Status: PASSED\n")
            else:
                print("Status: FAILED\n")

if __name__ == '__main__':
    functions_to_test = [set_solution, hash_solution]
    run_tests(testcases, functions_to_test)