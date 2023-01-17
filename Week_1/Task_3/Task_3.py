import re

ENTER = '\n'


def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
        return content


def write_data(out_file_name, file_name):
    data = ''
    with open(out_file_name, "w") as file:
        file.writelines(data)


def add_enters(file_name):
    content = read_data(file_name)
    pattern = r'[A-Za-z]'
    row = []
    match = re.findall(pattern=pattern, string=content)
    for index, i in enumerate(content, start=1):
        if index % 20 == 0 and index == 1:
            if i in match:
                row.append(content[:index - 1])
                content = content.replace(content[0:index - 1], '')
                print(index, row)
            elif i == ' ':
                row.append(content[:index])
                content = content.replace(content[0:index], '')
                print(index, row)


if __name__ == '__main__':
    # write_data("output.txt", "input.txt")
    add_enters("input.txt")
