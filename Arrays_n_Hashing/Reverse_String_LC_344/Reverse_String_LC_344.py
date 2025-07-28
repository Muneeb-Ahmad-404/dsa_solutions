from dsa_solutions.testing import test

def loops(attributes):
    s = attributes[0]

    i = 0
    j = len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

    
if __name__ == '__main__':    
    testcases = [
    [[[]], []],
    [[['a']], ['a']],
    [[['a', 'b', 'c', 'd']], ['d', 'c', 'b', 'a']],
    [[['h', 'e', 'l', 'l', 'o']], ['o', 'l', 'l', 'e', 'h']],
    [[['z', 'z', 'z', 'z', 'z']], ['z', 'z', 'z', 'z', 'z']],
    [[['r', 'a', 'c', 'e', 'c', 'a', 'r']], ['r', 'a', 'c', 'e', 'c', 'a', 'r']],
    [[['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '1', '2', '3']], 
     ['3', '2', '1', '!', 'd', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H']],
    # [[['A'] * 100000], ['A'] * 100000], 
    ]

    functions = [loops]
    test(testcases, functions)