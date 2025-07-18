from dsa_solutions.testing import test
from collections import defaultdict

# def brute_force(atts):
#     s = str(atts[0])
#     t = str(atts[1])
#     if len(s) != len(t):
#         return False
#     i = 0
#     while i<len(s):
#         j = 0
#         i = 0
#         while j < len(t):
#             if s[i] == t[j]:
#                 s.pop(i)
#                 t.pop(j)
#                 i, j = 1, 0
#                 break
#             j += 1
#         if i == 1: 
#             i = 0
#             continue
#         return False
#     return s == [] and t == []    #is valid but would require too much of the time

def sorting(attributes):
    s = list(attributes[0])
    t = list(attributes[1])

    s.sort(), t.sort()
    return s == t

def hash1(attributes):
    s = str(attributes[0])
    t = str(attributes[1])

    hash_s = defaultdict(int)
    for value in s:
        hash_s[value] += 1

    hash_t = defaultdict(int)
    for value in t:
        hash_t[value] += 1
        
    return hash_s == hash_t

def hash2(attributes):
    s = attributes[0]
    t =attributes[1]

    hash = defaultdict(int)
    for value in s:
        hash[value] += 1

    for value in t:
        hash[value] -= 1

    for key in hash:
        if hash[key] != 0:
            return False
    return True     
        


if __name__ == '__main__':
    test_cases = [
    (("abc", ""), False),
    (("", "xyz"), False),
    (("", ""), True),
    (("Listen", "silent"), False),
    (("Hello", "oHell"), True),
    (("ABC", "BCA"), True),
    (("Apple", "apple"), False),
    (("你好", "好你"), True),
    (("😂😊", "😊😂"), True),
    (("שלום", "מוש"), False),
    (("a!", "!a"), True),
    (("123", "321"), True),
    (("ab c", "ac b"), True),
    (("café", "face"), False),
    (("Resumé", "resume"), False),
    (("aaa", "aaa"), True),
    (("aabb", "bbaa"), True),
    (("aaa", "aab"), False),
    (("abc", "abd"), False),
    (("python", "java"), False),
    (("abc", "abcd"), False),
    (("abcdef", "abcde"), False),
    (("a" * 50000 + "b" * 50000, "b" * 50000 + "a" * 50000), True),
    (("abcdef" * 10000, "fedcba" * 10000), True),
    (("x" * 100000 + "y", "x" * 100000 + "z"), False),
    (("longstringwithmanycharacters", "anotherlongstring"), False),
    (("abcdefg" * 15000 + "h", "abcdefg" * 15000 + "i"), False)
]
    
functions = [sorting, hash1, hash2]
test(test_cases, functions)
    