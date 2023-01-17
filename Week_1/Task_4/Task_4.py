import re

COMMA = ", "
ENTER = "\n"


def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
        return content


def write_data(out_file_name, file_name):
    data = add_enters(file_name)
    with open(out_file_name, "w") as file:
        file.writelines(data)


def find_count_symbols(file_name):
    pattern = r'[A-Za-z]'
    content = read_data(file_name)
    symbols = re.findall(pattern=pattern, string=content)
    visited = set()
    duplicates_set = {}
    key = [x for x in symbols if x in visited or (visited.add(x) or False)]

    for index, i in enumerate(key):
        duplicates_set[key[index]] = 0

    for x in key:
        if x in duplicates_set:
            duplicates_set[x] += 1
        else:
            duplicates_set[x] = 1

    return duplicates_set


def sorted_top(file_name):
    content_set = find_count_symbols("input.txt")
    return sorted(content_set.items(), key=lambda x: x[-1], reverse=True)


def add_enters(file_name):
    content = list(sorted_top(file_name))
    row = []
    for i in content:
        for index, x in enumerate(i):
            if type(x) == int:
                y = str(x)
                row.append(y + ENTER)
            else:
                row.append(x[index] + COMMA)
    return row[:20]


if __name__ == '__main__':
    write_data("output.txt", "input.txt")
