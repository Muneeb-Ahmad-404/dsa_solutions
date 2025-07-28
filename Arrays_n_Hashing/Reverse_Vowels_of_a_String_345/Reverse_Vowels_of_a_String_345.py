from dsa_solutions.testing import test
def two_pointer(attributes):
    s = attributes[0]

    s = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    i, j = 0, len(s)-1
    while i<j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            continue
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1

    return ''.join(s)

if __name__ == '__main__':
    testcases = [
    [[""], ""],
    [["rhythm"], "rhythm"],
    [["bcdfg"], "bcdfg"],
    [["aeiou"], "ouiea"],
    [["AEIOU"], "UOIEA"],
    [["AaEeIiOoUu"], "uUoOiIeEaA"],
    [["hello"], "holle"],
    [["leetcode"], "leotcede"],
    [["DesignAlgorithms"], "DisognAlgirethms"],
    [["a"], "a"],
    [["z"], "z"],
    # [["b" * 100000], "b" * 100000], 
    # [["a" * 100000], "a" * 100000],
    # [["abcdefghijklmnopqrstuvwxyz" * 5000], "zyxwvuHtsrqpOnmlkjiGfedcbA" * 5000], 
    ]

    functions = [two_pointer]

    test(testcases, functions)