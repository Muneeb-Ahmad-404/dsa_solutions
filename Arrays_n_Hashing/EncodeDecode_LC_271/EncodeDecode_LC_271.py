from dsa_solutions.testing import test

def encode(strs):
    encoded = ""
    for data in strs:
        length = len(data)
        length = str(length)
        encoded += length+'#'+data
    return encoded

def decode(s):
    decoded = []
    i = 0
    while i < len(s):
        length = 0
        j = i
        while s[j] != '#':
            length *= 10
            length += int(s[j])
            j += 1   
        i = j+1
        data = s[i:i+length]
        decoded.append(data)
        i += length
    return decoded

def runner(strs):
    s = encode(strs)
    decoded = str(decode(s)) 
    return (s+decoded)


if __name__ == '__main__':
    test_cases = [
    (['ali', 'imran', 'dsaf', 'afdsa12:#'], ['ali', 'imran', 'dsaf', 'afdsa12:#']),
    ([], []),
    (['3241wqer#@#'], ['3241wqer#@#']),
    (['', ''], ['', '']),
    ([''], ['']),
    (['34twt', '', 'wet435'], ['34twt', '', 'wet435']),
    (['124q35q235fst3q252q353q45gser', '523#@@#$214 ergwt43re'], ['124q35q235fst3q252q353q45gser', '523#@@#$214 ergwt43re']),
    ]

    functions = [runner]

    test(test_cases, functions)

