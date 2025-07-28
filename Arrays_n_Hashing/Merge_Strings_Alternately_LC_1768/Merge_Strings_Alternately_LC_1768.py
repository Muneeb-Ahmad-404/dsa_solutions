from dsa_solutions.testing import test
def brute_force(attributes):
    word1, word2  = attributes[0], attributes[1]

    result = ""
    length = min(len(word1), len(word2))
    i = 0
    while i<length:
        result += word1[i]
        result += word2[i]
        i += 1

    result += word1[i:]
    result += word2[i:]
    return result

if __name__ == '__main__':
    testcases = [
    [["abc", "abc"], "aabbcc"],
    [["", ""], ""],
    [["abc", ""], "abc"],
    [["", "xyz"], "xyz"],
    [["a" * 50000, "b" * 50000], ("ab" * 50000)],
    [["a", "b"], "ab"],
    [["a", "xyz"], "axyz"],
    [["abc", "z"], "azbc"],
    [["hello", "world"], "hweolrllod"]
    ]
    
    functions = [brute_force]
    test(testcases, functions)
