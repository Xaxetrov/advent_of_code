import os


def read_input(filename: str) ->  'list[tuple[str]]':
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        return f.read().splitlines()


def split_pockets(bags):
    result = []
    for bag in bags:
        result.append((set(bag[:len(bag)//2]), bag[len(bag)//2:]))  # Could also setify second part, it is a tradeof
    return result


def split_groups(bags):  # Could also be done with zip and iter, maybe less readable
    grouped_bags = []
    for i in range(0, len(bags), 3):
        grouped_bags.append((bags[i:i + 3]))
    return grouped_bags


def priority(letter: str):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


# Part 1
def sum_pocket_intersection(bags: 'tuple[set[str]]') -> int:
    result = 0
    for bag in bags:
        (intersection,) = bag[0].intersection(bag[1])
        result += priority(intersection)
    return result


# Part 2
def sum_badge_intersection(bag_groups: 'list[list[str]]'):
    result = 0
    for bag_group in bag_groups:
        (intersection,) = set(bag_group[0]).intersection(bag_group[1]).intersection(bag_group[2])
        result += priority(intersection)
    return result


if __name__ == '__main__':
    bags = read_input('day3.txt')
    
    splited_bags = split_pockets(bags)
    print(sum_pocket_intersection(splited_bags))

    grouped_bags = split_groups(bags)
    print(sum_badge_intersection(grouped_bags))
    