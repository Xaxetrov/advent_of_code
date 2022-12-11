from collections import deque
from copy import deepcopy
from math import lcm
from operator import add, mul
import os
import re


def read_input(filename: str) ->  'list[Monkey]':
    monkeys = []
    number_regexp = re.compile(r'\d+')
    
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        monkey_infos = f.read().split('\n\n')
    
    for monkey_info in monkey_infos:
        lines = monkey_info.splitlines()
        operation_value_raw = number_regexp.search(lines[2])
        monkeys.append(Monkey(
            deque(map(int, number_regexp.findall(lines[1]))),
            add if '+' in lines[2] else mul,
            int(operation_value_raw.group()) if operation_value_raw else None,
            int(number_regexp.search(lines[3]).group()),
            int(number_regexp.search(lines[4]).group()),
            int(number_regexp.search(lines[5]).group())
        ))

    return monkeys


class Monkey:
    def __init__(self, items: 'deque[int]', operation, operation_value, test, next_true, next_false) -> None:
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test = test
        self.next_true, self.next_false = next_true, next_false
        self.inspection_counter = 0

    def inspect(self, modulo):
        item = self.items.popleft()
        increased_item = self.operation(item, item) if self.operation_value is None else (self.operation(item, self.operation_value))
        return increased_item % modulo if modulo is not None else increased_item // 3

    def throw(self, item: int, monkeys: 'list[Monkey]'):
        if item % self.test == 0:
            monkeys[self.next_true].items.append(item)
        else:
            monkeys[self.next_false].items.append(item)

    def take_turn(self, monkeys: 'list[Monkey]', modulo):
        self.inspection_counter += len(self.items)
        while self.items:
            inspected_item = self.inspect(modulo)
            self.throw(inspected_item, monkeys)


def play_round(monkeys: 'list[Monkey]', part_2 = False):
    modulo = lcm(*(monkey.test for monkey in monkeys)) if part_2 else None
    for monkey in monkeys:
        monkey.take_turn(monkeys, modulo)


def top_monkeys(monkeys: 'list[Monkey]'):
    top_1, top_2 = sorted(monkeys, key=lambda x: x.inspection_counter, reverse=True)[:2]
    return top_1.inspection_counter * top_2.inspection_counter


if __name__ == '__main__':
    monkeys_1 = read_input('day11.txt')
    monkeys_2 = deepcopy(monkeys_1)

    # Part 1
    for round in range(20):
        play_round(monkeys_1)
    print(top_monkeys(monkeys_1))

    # Part 2
    for round in range(10000):
        play_round(monkeys_2, True)
    print(top_monkeys(monkeys_2))