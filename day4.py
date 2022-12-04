import os


def read_input(filename: str) ->  'list[tuple[str]]':
    result = []
    
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        
        for line in f.read().splitlines():
            assignment_a, assignment_b = line.split(',')
            result.append([[int(value_a) for value_a in assignment_a.split('-')], [int(value_b) for value_b in assignment_b.split('-')]])

    return result


# Part 1
def is_assignment_pair_contained(assignment_a, assignment_b):
    return assignment_a[0] <= assignment_b[0] and assignment_a[1] >= assignment_b[1]\
        or assignment_a[0] >= assignment_b[0] and assignment_a[1] <= assignment_b[1]


# Part 2
def is_assignment_pair_overlapped(assignment_a, assignment_b):
    return not (assignment_a[0] > assignment_b[1] or assignment_a[1] < assignment_b[0])


def count_pairs_if(assignments, condition):
    return sum(1 for pair in assignments if condition(pair[0], pair[1]))



if __name__ == '__main__':
    assignments = read_input('day4.txt')

    print(count_pairs_if(assignments, is_assignment_pair_contained))
    print(count_pairs_if(assignments, is_assignment_pair_overlapped))
