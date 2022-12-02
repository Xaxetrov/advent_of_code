from enum import Enum
import os

SCORE_1 = {  # Round 1. Only 9 combinations.
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6,
}

SCORE_2 = {  # Round 2. Still only 9 combinations.
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7,
}


def read_input(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    round_lines = read_input('day2.txt')
    
    print(sum([SCORE_1[round_line] for round_line in round_lines]))
    print(sum([SCORE_2[round_line] for round_line in round_lines]))
