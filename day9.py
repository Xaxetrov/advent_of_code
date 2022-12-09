from functools import reduce
from math import copysign
import os


def read_input(filename):
    direction_codes = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    instructions = []
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        for line in f.read().splitlines():
            direction, repetition = line.split(' ')
            instructions.append((direction_codes[direction], int(repetition)))
    return instructions


sign = lambda x: int(copysign(1, x))


def move_rope(rope: 'list[list[int]]', direction: 'tuple[int]'):
    rope[0][0] += direction[0]
    rope[0][1] += direction[1]

    for index in range(1, len(rope)):
        vector = (rope[index - 1][0] - rope[index][0], rope[index - 1][1] - rope[index][1])
        
        if vector[0] == 0 or vector[1] == 0:
            if abs(vector[0]) >= 2:
                rope[index][0] += sign(vector[0])
            elif abs(vector[1]) >= 2:
                rope[index][1] += sign(vector[1])
        elif abs(vector[0]) != 1 or abs(vector[1]) != 1:
            rope[index][0] += sign(vector[0])
            rope[index][1] += sign(vector[1])


def log_tail(rope: 'list[list[int]]', tails: 'dict[set[tuple]]', index: int):
    tails[index].add(tuple(rope[index]))


if __name__ == '__main__':
    instructions = read_input('day9.txt')

    rope = [[0, 0] for _ in range(10)]
    tails = {
        1: set(),
        9: set()
    }

    for direction, repetition in instructions:
        for _ in range(repetition):
            move_rope(rope, direction)
            log_tail(rope, tails, 1) # Part 1
            log_tail(rope, tails, 9) # Part 2

    print(len(tails[1]))
    print(len(tails[9]))
