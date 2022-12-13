from functools import cmp_to_key
import os

def read_input(filename: str) -> '':
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        string_pairs = f.read().split('\n\n')
    return [[*map(eval, string_pair.split())] for string_pair in string_pairs]


def compare(first, second):
    match first, second:
        case int(), int():
            return 1 if first > second else -1 if first < second else 0
        case list(), int():
            return compare(first, [second])
        case int(), list():
            return compare([first], second)
        case list(), list():
            for element_comparison in map(compare, first, second):
                if element_comparison != 0:
                    return element_comparison
            return compare(len(first), len(second))


def sum_ordered(pairs: 'list[list[list]]'):
    compared = [compare(*pair) for pair in pairs]
    return sum(i+1 for i, v in enumerate(compared) if v == -1)


if __name__ == '__main__':
    pairs = read_input('day13.txt')
    
    # Part 1
    print(sum_ordered(pairs))

    # Part 2
    all_packets = sum(pairs, [[2], [6]])
    sorted_packets = sorted(all_packets, key=cmp_to_key(compare))
    print( (sorted_packets.index([2]) + 1) * (sorted_packets.index([6]) + 1) )