from collections import defaultdict
def hash(words, chars):
    dict = defaultdict(int)
    for char in chars:
        dict[char] += 1
    result = 0
    for word in words:
        dict_word = defaultdict(int)
        for char in word:
            dict_word[char] += 1
        is_formable = True
        for char, count in dict_word.items():
            if dict[char] < count:
                is_formable = False
                break
        if is_formable:
            result += len(word)
    return result

testcases = [
    [["cat", "bt", "hat"], "atach", 6],
    [["hello", "world", "leetcode"], "welldonehoneyr", 10],
    [["ab", "aa", "a"], "aab", 5],
    [["a", "b", "aa"], "aab", 4],
    [["a", "b", "c"], "abc", 3],
    [["a", "b", "c"], "def", 0],
    [[], "abc", 0],
    [["a", "b", "c"], "", 0],
    [["abcd"], "dcba", 4],
    [["applepie"], "apple", 0],
    [["ace", "bdf"], "abcde", 3],
]

def run_tests(test_cases, functions_to_test):
    for i, (words, chars, expected_output) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Words: {words}")
        print(f"Chars: {chars}")

        for func in functions_to_test:
            print(f"Running function: {func.__name__}")
            actual_output = func(words, chars)

            print(f"Expected: {expected_output}")
            print(f"Actual: {actual_output}")

            if actual_output == expected_output:
                print("Status: PASSED\n")
            else:
                print("Status: FAILED\n")

if __name__ == '__main__':
    functions_to_test = [hash]
    run_tests(testcases, functions_to_test)