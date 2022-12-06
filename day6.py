from collections import deque
import os


def read_input(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        return f.read()


def find_unique_sequence(string: str, sequence_size: int):
    buffer = deque(maxlen=sequence_size)
    for i, character in enumerate(string):
        buffer.append(character)
        if len(set(buffer)) == sequence_size:
            return i + 1


if __name__ == '__main__':
    line = read_input('day6.txt')
    
    print(find_unique_sequence(line, 4))
    print(find_unique_sequence(line, 14))
