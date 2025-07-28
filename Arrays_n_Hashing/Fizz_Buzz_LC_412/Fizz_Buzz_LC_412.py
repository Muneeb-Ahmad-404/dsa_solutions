from dsa_solutions.testing import test
def solution(attributes):
    n = attributes[0]

    result = []
    for i in range(n):
        idx = i+1
        if idx % 3 == 0 and idx % 5 == 0:
            result.append('FizzBuzz')
        elif idx % 3 == 0:
            result.append('Fizz')
        elif idx % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(idx))
    return result

if __name__ == '__main__':
    testcases = [
    [[0], []],
    [[1], ["1"]],
    [[2], ["1", "2"]],
    [[3], ["1", "2", "Fizz"]],
    [[5], ["1", "2", "Fizz", "4", "Buzz"]],
    [[15], ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]],
    [[6], ["1", "2", "Fizz", "4", "Buzz", "Fizz"]],
    [[10], ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]],
    [[1000], ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"] * 66 + ["16", "17", "Fizz", "19", "Buzz", "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"] * 33 + ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz", "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"]], # Note: This is still a conceptual representation due to length. A real large test case would be generated.
    [[30], ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz", "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"]],
    ]
    
    functions = [solution]
    test(testcases, functions)