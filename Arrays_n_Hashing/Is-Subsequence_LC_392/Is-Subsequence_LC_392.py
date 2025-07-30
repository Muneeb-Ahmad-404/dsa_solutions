def two_pointer(s, t):

    s_ptr, t_ptr = 0 ,0 

    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1
    
    return s_ptr == len(s)
        
if __name__ == '__main__':
    def test(testcases, functions):
        for i, (input_pair, expected_output) in enumerate(testcases):
            s_val, t_val = input_pair
            for function in functions:
                print(f"--- Running {function.__name__} ---")
                print(f'Test {i} \nInput: s="{s_val}", t="{t_val}"') 
                result = function(s_val, t_val) # Pass s and t directly
                print(f'Expected: {expected_output} \nOutput: {result}')
                if result == expected_output:
                    print("Status: PASSED\n")
                else:
                    print("Status: FAILED\n")

    testcases = [
        # Basic true cases
        [["ace", "abcde"], True],
        [["abc", "ahbgdc"], True],
        [["", "abc"], True], # Empty string is always a subsequence
        [["a", "a"], True],
        [["aa", "aa"], True],
        [["ab", "baab"], True], # Characters are scattered but order is maintained

        # Basic false cases
        [["aec", "abcde"], False], # 'e' comes before 'c'
        [["axc", "ahbgdc"], False], # 'x' not in 't'
        [["abc", ""], False],     # s cannot be subsequence of empty t
        [["a", "b"], False],
        [["abc", "acb"], False], # Same chars, wrong order
        [["aab", "aba"], False], # Anagram, but not subsequence due to order/frequency
        [["b", "a"], False],

        # Longer strings
        [["abcdef", "axbyczdwef"], True],
        [["longest", "ghlongtesxyt"], True], # Non-contiguous
        [["test", "ttest"], True], # 't' appears twice in s, only one 't' needed from t

        # s is longer than t
        [["abcde", "abc"], False],

        # s and t are identical
        [["hello", "hello"], True],
    ]

    functions = [two_pointer]
    test(testcases, functions)