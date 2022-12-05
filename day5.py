from collections import deque
import copy
from itertools import groupby
import os


def read_input(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        lines = f.read().splitlines()
        return [list(group) for k, group in groupby(lines, lambda x: x == '') if not k]


def build_stacks(lines):
    stacks = [deque() for i in range(len(lines))]

    for line in lines[:-1]:
        for position in range(0, len(line), 4):
            if line[position + 1] != ' ':
                stacks[position // 4].append(line[position + 1])

    for stack in stacks:
        stack = stack.reverse()
    return stacks


def build_operations(lines: 'list[str]'):
    operations = []
    for line in lines:
        splitted_line = line.split()
        operations.append((int(splitted_line[1]), int(splitted_line[3]) - 1, int(splitted_line[5]) - 1))
    return operations


def follow_procedure_1(stacks: 'list[deque]', operations):
    for operation in operations:
        for repetition in range(operation[0]):
            stacks[operation[2]].append(stacks[operation[1]].pop())


def follow_procedure_2(stacks: 'list[deque]', operations):
    for operation in operations:
        temp = deque()
        for repetition in range(operation[0]):
            temp.appendleft(stacks[operation[1]].pop())
        stacks[operation[2]].extend(temp)


def get_tops(stacks: 'list[deque]'):
    return ''.join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    stack_lines, operation_lines = read_input('day5.txt')
    
    stacks_1 = build_stacks(stack_lines)
    stacks_2 = copy.deepcopy(stacks_1)
    operations = build_operations(operation_lines)

    follow_procedure_1(stacks_1, operations)
    print(get_tops(stacks_1))

    follow_procedure_2(stacks_2, operations)
    print(get_tops(stacks_2))
