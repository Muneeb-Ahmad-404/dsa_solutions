from dsa_solutions.testing import test

def simple_loop(attributes):
    operations = attributes[0]

    x = 0
    for s in operations:
        if s[0] == '+' or s[1] == '+':
            x += 1
        else:
            x -= 1
    return x

if __name__ == '__main__':
    test_cases = [
    ([[]], 0),
    ([[1] * 100], 100),
    ([[-1, -1, -1, -1]], 0),
    ([[1, 2, 3, 4]], 10),
    ]

    functions = [simple_loop]

    test(test_cases, functions)
    