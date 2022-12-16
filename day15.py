import os
import re


def read_input(filename: str) -> list[zip]:
    input_path = os.path.join(os.path.dirname(__file__), filename)
    sensors = []
    beacons = set()
    with open(input_path, 'r') as f:
        for line in f.read().splitlines():
            match = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
            sensors.append(Sensor(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
            beacons.add((int(match.group(3)), int(match.group(4))))
    return sensors, beacons


class Sensor:
    def __init__(self, x, y, b_x, b_y) -> None:
        self.position = (x, y)
        self.range = manhattan_distance(self.position, (b_x, b_y))


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def merge_segments(segments: list[list[int]]):
    segments.sort(key=lambda segment: segment[0])
    merged = []
    for segment in segments:
        if not merged or merged[-1][1] < segment[0]:
                merged.append(segment)
        else:
            merged[-1][1] = max(merged[-1][1], segment[1])
    return merged


def get_line_coverage(sensors: list[Sensor], line_y):
    covered = []
    for sensor in sensors:
        wide = sensor.range - abs(sensor.position[1] - line_y)
        if wide >= 0:
            covered.append([sensor.position[0] - wide, sensor.position[0] + wide + 1])
    
    return merge_segments(covered)
    


def coverage_sum(coverage, beacons: set[tuple[int]], line_y):
    covered_sum = sum(segment[1] - segment[0] for segment in coverage)
    for beacon in beacons:
        if beacon[1] == line_y:
            for covered_segment in coverage:
                if covered_segment[0] <= beacon[0] < covered_segment[1]:
                    covered_sum -= 1
    return covered_sum


if __name__ == '__main__':
    sensors, beacons = read_input('day15.txt')

    # Part 1
    y = 2000000
    coverage = get_line_coverage(sensors, y)
    print(coverage_sum(coverage, beacons, y))

    # Part 2 - Takes 2 - 3 minutes
    for y in range(4000001):
        coverage = get_line_coverage(sensors, y)
        couples = list(zip(coverage, coverage[1:]))
        for couple in couples:
            if couple[1][0] - couple[0][1] == 1:
                print(couple[0][1], y)
                exit(0)
