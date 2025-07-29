from dsa_solutions.testing import test
def two_pointer(attributes):
    s = attributes[0]

    left, right = 0, len(s)-1
    while left<right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    testcases = [
    [[""], True],
    [["A man, a plan, a canal: Panama"], True],
    [["race a car"], False],
    [["Was it a car or a cat I saw?"], True],
    [[""], True],
    [["abcdefghijklmnopqrstuvwxyz" * 50000 + "zyxwVutsrqponmlkjihgfedcba" * 50000], True],
    [["helloolleh" * 100000], True],
    [["abcba"], True],
    [["madam"], True],
    [["noon"], True],
    [["abc"], False],
    [["ab"], False],
    [[".,"], True],
    [["!@#$%^&*()"], True],
    [[".,a,"], True],
    [["!!!!a!!!!"], True],
    [["aaaaa"], True],
    [["bbbbb"], True],
    [["!!!!"], True]
    ]

    functions = [two_pointer]
    test(testcases, functions)
    


