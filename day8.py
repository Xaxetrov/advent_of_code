from functools import reduce
import os


def read_input(filename):
    forest = []
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        for line in f.read().splitlines():
            temp = []
            for char in line:
                temp.append(int(char))
            forest.append(temp)
    return forest


# Not optimal but quite readable
def bruteforce_both_solutions(forest):

    part_1 = 0
    part_2 = 0

    for row in range(len(forest)):
        for column in range(len(forest[0])):
            tree = forest[row][column]

            aligned_trees = [  # Not scalable but I am ok with total iterations <= 1M here
                forest[row][column+1:],
                forest[row][:column][::-1],
                [tree_line[column] for tree_line in forest[row+1:]],
                [tree_line[column] for tree_line in forest[:row]][::-1]
            ]

            # Part 1
            visible_others = [[other_tree >= tree for other_tree in direction] for direction in aligned_trees]
            part_1 += 1 if any(not any(visible_others_direction) for visible_others_direction in visible_others) else 0

            # Part 2
            viewing_distances = [(direction.index(True) + 1) if True in direction else len(direction) for direction in visible_others]
            score = reduce(lambda x, y: x*y, viewing_distances)
            if score > part_2:
                part_2 = score

    return part_1, part_2


if __name__ == '__main__':
    forest = read_input('day8.txt')
    
    print(bruteforce_both_solutions(forest))
