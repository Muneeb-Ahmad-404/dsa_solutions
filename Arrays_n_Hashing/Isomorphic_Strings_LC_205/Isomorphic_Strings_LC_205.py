from dsa_solutions.testing import test

def hash(attributes):
    s = attributes[0]
    t = attributes[1]

    if len(s) != len(t):
        return False

    hash_s = {}
    hash_t = {}

    for i in range(len(s)):
        if hash_s.get(s[i]) != None:
            if hash_s[s[i]] != t[i]:
                return False
        hash_s[s[i]] = t[i]

    for i in range(len(s)):
        if hash_t.get(t[i]) != None:
            if hash_t[t[i]] != s[i]:
                return False
        hash_t[t[i]] = s[i]

    return True

if __name__ == '__main__':

    testcases = [
        [["egg", "add"], True],
        [["foo", "bar"], False],
        [["paper", "title"], True],
        [["ab", "a"], False],
        [["ab", "xx"], False],
        [["abc", "bbb"], False],
        [["a", "z"], True],
        [["", ""], True],
        [["abcabc", "xyzxya"], False],
        [["abcdef", "abcdef"], True],
        [["abcdef", "abccde"], False],
        [["aaaaa", "bbbbb"], True],
        [["aA", "bB"], True],
        [["Aa", "bB"], True],
        [["aA", "aa"], False],
    ]

    functions = [hash]
    test(testcases, functions)

