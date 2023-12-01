DIGIT_PATTERNS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def main(input_file_name, convert_words):
    with open(input_file_name) as input_file:
        lines = [line.strip() for line in input_file.readlines() if line != '\n']

    if convert_words:
        lines = [convert(line) for line in lines]

    total = sum([
        int(next(x for x in line if x.isnumeric())
        + next(x for x in reversed(line) if x.isnumeric()))
    for line in lines])

    return total


def convert(line):
    first_number = min([line.find(d) for d in DIGIT_PATTERNS.values() if line.find(d) != -1], default=None)
    last_number = max([line.rfind(d) for d in DIGIT_PATTERNS.values() if line.rfind(d) != -1], default=None)
    first_word = None
    last_word = None
    for word in DIGIT_PATTERNS:
        iloc = line.find(word)
        if iloc != -1 and (first_number is None or iloc < first_number) and (not first_word or iloc < first_word[0]):
            first_word = (iloc, word)
        iloc = line.rfind(word)
        if iloc != -1 and (last_number is None or iloc > last_number) and (not last_word or iloc > last_word[0]):
            last_word = (iloc, word)
    if first_word:
        line = DIGIT_PATTERNS[first_word[1]] + line
    if last_word and last_word != first_word:
        line = line + DIGIT_PATTERNS[last_word[1]]
    return line


if __name__ == '__main__':
    print(main('day01/example1.txt', False))
    print(main('day01/input.txt', False))
    print(main('day01/example2.txt', True))
    print(main('day01/input.txt', True))
