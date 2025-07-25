from dsa_solutions.testing import test
from collections import defaultdict

def brute_force(attributes):
    jewels = attributes[0]
    stones = attributes[1]

    count = 0
    for stone in stones:
        for jewel in jewels:
            if jewel == stone:
                count += 1
                break
    return count

def hash_map(attributes):
    jewels = attributes[0]
    stones = attributes[1]

    hash_jewel = defaultdict(int)
    for jewel in jewels:
        hash_jewel[jewel] = 1
    
    count = 0
    for stone in stones:
        count += hash_jewel[stone]
    return count



if __name__ == '__main__':
    testcases = [
    [["aA", ""], 0],
    [["", "aAAbbbb"], 0],
    [["", ""], 0],
    [["abc", "DEFghi"], 0],
    [["aAbBcC", "aAbBcC"], 6],
    [["aA", "aaaaAA"], 6],
    [["xY", "xYyXyYxX" * 10000], 40000],
    [["".join(chr(i) for i in range(33, 127)) * 5, "Hello World!123"], 14],
    [["aAb", "abCDefaAbB"], 5],
    [["A", "AAAAAAbbbbb"], 6],
    [["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "x"], 1],
    ]

    functions = [brute_force, hash_map]
    test(testcases, functions)