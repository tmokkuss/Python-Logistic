ENTER = '\n'


def read_data(file_name):
    with open(file_name) as file:
        content = file.read().splitlines()
        return content


def write_data(out_file_name, file_name):
    data = sort_data(file_name)
    with open(out_file_name, "w") as file:
        file.writelines(data)


def sort_data(file_name):
    data = read_data(file_name)
    content = []
    for i in data:
        row = i + ENTER
        content.append(row)

    def function(x):  # lambda x: float(x[6:8])
        first_value = float(x[6:8])
        return first_value

    return sorted(content, key=function)


if __name__ == '__main__':
    write_data("output.txt", "input.txt")
