from collections import defaultdict, deque
import os


directories = set()
sizes = defaultdict(int)


def read_input(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        return f.read().splitlines()


def build_sizes(lines: 'list[str]'):
    dir_stack = deque()

    for line in lines:
        words = line.split(' ')

        if words[0] == '$':
            if words[1] == 'cd':
                if words[2] == '..':
                    dir_stack.pop()
                else:
                    dir_stack.append(words[2])

        else:
            if words[0] == 'dir':
                directories.add('/'.join(dir_stack) + '/' + words[1])
            
            else:
                iterative_path = ''
                for dir in dir_stack:
                    iterative_path += dir
                    sizes[iterative_path] += int(words[0])
                    iterative_path += '/'
                sizes[iterative_path + words[1]] = int(words[0])


# Part 1
def sum_small_directories():
    return(sum(sizes[directory] for directory in directories if sizes[directory] <= 100000))


# Part 2
def find_directory_to_delete():
    to_find = sizes['/'] - 40000000
    return min(sizes[directory] for directory in directories if sizes[directory] >= to_find)


if __name__ == '__main__':
    lines = read_input('day7.txt')
    build_sizes(lines)
    print(sum_small_directories())
    print(find_directory_to_delete())
