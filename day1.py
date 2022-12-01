import os


def read_input(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        line_groups = f.read().split('\n\n')
        return [[int(value) for value in group.splitlines()] for group in line_groups]


# First question
def biggest_group_sum(groups):
    return max([sum(group) for group in groups])


# Second question
def biggest_3_group_sum(groups):
    summed_groups = [sum(group) for group in groups]
    sorted_summed_groups = sorted(summed_groups, reverse=True)
    return sum(sorted_summed_groups[:3])


if __name__ == '__main__':
    my_input = read_input('day1.txt')


    print(biggest_group_sum(my_input))
    print(biggest_3_group_sum(my_input))
