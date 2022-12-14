from collections import deque
from copy import deepcopy
from math import lcm
from operator import add, mul
import os
import re


def read_input(filename: str) -> list[zip]:
    input_path = os.path.join(os.path.dirname(__file__), filename)
    rocks = []
    with open(input_path, 'r') as f:
        for line in f.read().splitlines():
            points = [list(map(int, p.split(","))) for p in line.split(" -> ")]
            rocks.append(zip(points, points[1:]))
    return rocks
 

def build_cave(rocks: 'list[zip[tuple[int]]]') -> set[tuple[int]]:
    abyss = 0
    cave = set()
    for segments in rocks:
        for (x1, y1), (x2, y2) in segments:
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))
            abyss = max(abyss, y1)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    cave.add((x, y))
    return cave, abyss


def flow(cave: set[tuple[int]], unit: tuple[int], floor: int) -> tuple[tuple[int], bool]:
    if floor is not None and unit[1] == floor - 1:
        return unit, False

    elif (unit[0], unit[1] + 1) not in cave:
        return (unit[0], unit[1] + 1), True
    elif (unit[0] - 1, unit[1] + 1) not in cave:
        return (unit[0] - 1, unit[1] + 1), True
    elif (unit[0] + 1, unit[1] + 1) not in cave:
        return (unit[0] + 1, unit[1] + 1), True

    else:
        return unit, False


# Part 1
def has_sand_overflowed(unit: tuple[int], abyss: int) -> bool:
    return unit[1] >= abyss

# Part 2
def is_sand_stuck(unit: tuple[int], _):
    return unit == (500, 0)


def sand_capacity(cave: set[tuple[int]], abyss: int, stopping_condition: 'function', floor = None) -> int:
    fallen_sand = 0
    stop = False
    while not stop:
        
        unit = (500, 0)
        flowing = True
        
        while flowing and not stop:
            unit, flowing = flow(cave, unit, floor)
            stop = stopping_condition(unit, abyss)
        
        fallen_sand += not stop
        cave.add(unit)

    return fallen_sand


if __name__ == '__main__':
    rocks = read_input('day14.txt')
    cave, abyss = build_cave(rocks)
    cave2 = deepcopy(cave)

    print(sand_capacity(cave, abyss, has_sand_overflowed))

    print(sand_capacity(cave2, abyss, is_sand_stuck, abyss + 2) + 1)