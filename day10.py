import os


def read_input(filename: str) ->  'list[tuple[str]]':
    instructions = []
    
    input_path = os.path.join(os.path.dirname(__file__), filename)
    with open(input_path, 'r') as f:
        
        for line in f.read().splitlines():
            try:
                instruction, value = line.split(' ')
                instructions.append((instruction, int(value)))
                instructions.append(('noop', 0))
            except ValueError:
                instructions.append((line, 0))

    return instructions


def execute(instructions: list):
    cycle = 0
    pixel = x = 1
    next_logged_cycle = 20
    log = []
    drawing = '# '

    for instruction, value in instructions:
        cycle += 1
        
        # Part 1
        if cycle >= next_logged_cycle:
            log.append(x * next_logged_cycle)
            next_logged_cycle += 40

        # Part 2
        drawing += '# ' if x - 1 <= pixel <= x + 1 else '. '
        pixel += 1
        if pixel % 40 == 0:
            drawing += '\n'
            pixel = 0

        x += value

    return log, drawing


def format_screen(string: list):
    screen = ''
    for i in range(0, len(string), 40):
        screen += string[i:i+40] + '\n'
    return screen


if __name__ == '__main__':
    instructions = read_input('day10.txt')

    log, drawing = execute(instructions)

    print(sum(log))
    print(drawing)
