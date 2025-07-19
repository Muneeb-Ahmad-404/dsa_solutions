from dsa_solutions.testing import test

def loop(attributes):
    gain = attributes[0]
    max = 0   
    for i in range(0, len(gain)):
        if i == 0:
            if gain[i] > max:
                max = gain[i]
            continue
        gain[i] += gain[i-1]
        if gain[i] > max:
            max = gain[i]
    return max


def a_better_apporach(attributes):
    gain = attributes[0]
    current_altitude = 0    
    max_altitude_reached = 0 
    for g in gain:
        current_altitude += g 
        max_altitude_reached = max(max_altitude_reached,
        current_altitude) 

    return max_altitude_reached


if __name__ == '__main__':
    test_cases = [
    ([[-5, -2, -1]], 0),
    ([[]], 0),
    ([[2, 2, 2]], 6),
    ([[-1, -1, -1]], 0),
    ([[1] * 100], 100),
    ([[0, 0, 0]], 0),
    ]

    functions = [loop, a_better_apporach]
    test(test_cases, functions)