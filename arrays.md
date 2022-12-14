+ [MD-form](#md-form)

## MD-form

Написать программу, которая выводит на экран md-form, считывая с файла и образет новый файл в выводом.

```python
def read_data(file_name):
    file = open(file_name, 'r')
    content = file.read()
    return content


def prepare_md_title(data):
    splitted = data.split('\n')
    title, description = "", ""

    for line in splitted:
        if line.startswith('# title'):
            title = line.lstrip('# title')
        elif line.startswith('# description'):
            description = line.lstrip('# description')

    return title, description


def md_text_formatted(title, description, source_code):
    md_link = ''.join(title.lower().split())
    template = '+ [{}](#{})\n\n## {}\n\n{}\n\n```python\n{}\n```'

    return template.format(title, md_link, title, description, source_code)


def convert_to_md(data):
    data = content.split('# ---end---')
    titles, source_code = data[0], data[1]
    title, description = prepare_md_title(titles)
    result = md_text_formatted(title, description, source_code.lstrip())
    return result


def write_data(data):
    f = open('out.txt', "w+")
    f.write(data)
    f.close()
    return f


content = read_data('solution.txt')
md_content = convert_to_md(content)
print(f'{write_data(md_content)} Файл создан!')

```
