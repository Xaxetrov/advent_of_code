from collections import defaultdict
from functools import cache
import os
import re


# Global
valve_rates = {}
tunnels = defaultdict(list)


def read_input(filename: str):
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        for line in f.read().splitlines():
            match = re.match('Valve (..) has flow rate=(-?\d+); tunnels? leads? to valves? (.*)', line)
            valve_rates[match.group(1)] = int(match.group(2))
            for other in match.group(3).split(', '):
                tunnels[match.group(1)].append(other)

@cache
def max_leak(current, timer, opened: set, strategy: 'function'):
    if timer <= 0:
        return 0

    best_leak = 0

    for other in tunnels[current]:
        best_leak = max(
            best_leak,
            strategy(other, timer - 1, opened)
        )

    # Maybe open this valve
    if current not in opened and valve_rates[current] > 0:
        leak_if_opened = (timer - 1) * valve_rates[current]
        opened_if_open = set(opened)
        opened_if_open.add(current)

        for other in tunnels[current]:
            best_leak = max(
                best_leak,
                leak_if_opened + strategy(other, timer - 2, frozenset(opened_if_open))
            )
    
    return best_leak

@cache
def max_leak_alone(current, timer, opened: set):
    return max_leak(current, timer, opened, max_leak_alone)


@cache
def max_leak_with_friend(current, timer, opened: set):

    # Explore options left for friend
    # All options will be explored anyways
    if timer <= 0:
        return max_leak_alone('AA', 26, opened)

    return max_leak(current, timer, opened, max_leak_with_friend)


if __name__ == '__main__':
    read_input('day16.txt')
    print(max_leak_alone('AA', 30, frozenset()))
    print(max_leak_with_friend('AA', 26, frozenset()))
