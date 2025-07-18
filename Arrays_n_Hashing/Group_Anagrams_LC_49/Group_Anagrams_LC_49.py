import string
from dsa_solutions.testing import test

def sorting(attributes):
    strs = attributes[0]
    sorted = {}
    for i, data_str in enumerate(strs):
        data_str = list(data_str)
        data_str.sort()
        data_str = str(data_str)
        if data_str in sorted:
            sorted[data_str].append(strs[i])
            continue
        sorted[data_str] = [strs[i]]
    return list(sorted.values())


def hash(attributes):
    strs = attributes[0]
    print(strs )
    imprints = {}

    for idx, data_str in enumerate(strs):
        alpha = [0] * 26

        for i in range(len(data_str)):
            idx = ord(data_str[i]) - ord('a')
            alpha[idx] += 1
        
        imprint = tuple(alpha)

        if not imprint in imprints:
            imprints[imprint] = [data_str]
        else:
            imprints[imprint].append(data_str)

    return list(imprints.values())


        

if __name__ == '__main__':
    test_cases = [
    ([[]], []),
    ([["eat", "tea", "tan", "ate", "nat", "bat"]], [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]),
    ([["", "b", "", "a", "b"]], [["", ""], ["a"], ["b", "b"]]),
    ([["abc", "def", "ghi", "jklm"]], [["abc"], ["def"], ["ghi"], ["jklm"]]),
    ([
        [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a",
            "apple", "pleap", "banana", "anaban", "level", "evelL", "hello", "ollhe"
        ]
    ], [
        ["a", "a"], ["b", "b"], ["c", "c"], ["d", "d"], ["e", "e"], ["f", "f"], ["g", "g"], ["h", "h"], ["i", "i"], ["j", "j"],
        ["k", "k"], ["l", "l"], ["m", "m"], ["n", "n"], ["o", "o"], ["p", "p"], ["q", "q"], ["r", "r"], ["s", "s"], ["t", "t"],
        ["u", "u"], ["v", "v"], ["w", "w"], ["x", "x"], ["y", "y"], ["z", "z"],
        ["anaban", "banana"], ["apple", "pleap"], ["evelL", "level"], ["hello", "ollhe"]
    ]),
    ([
        [
            "a" * 100, "b" * 100, "c" * 100, "a" * 100,
            "abcdefghijklmnopqrstuvwxyz" * 4,
            "zyxwuvtsrqponmlkjihgfedcba" * 4
        ]
    ], [
        ["a" * 100, "a" * 100], ["b" * 100], ["c" * 100],
        ["abcdefghijklmnopqrstuvwxyz" * 4, "zyxwuvtsrqponmlkjihgfedcba" * 4]
    ]),
    ] 

    functions = [sorting, hash]

    test(test_cases, functions)