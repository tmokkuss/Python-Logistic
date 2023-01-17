import re


COMMA = ","
ENTER = "\n"


def read_data(file_name):
    with open(file_name) as file:
        content = file.read().splitlines()
        return content


def get_grade_and_name(file_name):
    content = read_data(file_name)
    name = ''
    grade = ''
    list_of_students = []
    pattern_for_get_name = r'[0-9.:]'
    for i in content:
        name = re.sub(pattern_for_get_name, "", i).strip(" ")
        grade = i[-1]
        list_of_students.append(name + COMMA + grade + ENTER)

    return list_of_students


def alphabetical_sorting(file_name):
    content = get_grade_and_name(file_name)
    return sorted(content, key=lambda x: x.split(" ")[0].upper())


def write_data(out_file_name, file_name):
    data = alphabetical_sorting(file_name)
    with open(out_file_name, "w") as file:
        file.writelines(data)


if __name__ == '__main__':
    write_data("output.csv", "data.tdxt")
