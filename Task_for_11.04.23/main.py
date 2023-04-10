import random
import requests
import csv


def write_data(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def generate_ids(data_len):
    l = [str(random.randint(0, 99999)) for _ in range(data_len)]
    return l


def generate_salary(data_len):
    l = [str(random.randint(100000, 999999)) for _ in range(data_len)]
    return l


def generate_month(data_len):
    months = [str(random.randint(1, 12)) for _ in range(data_len)]
    return months


def generate_users(data_len):
    url = "https://randomuser.me/api/"
    params = {'results': data_len}
    response = requests.get(url, params=params)
    data = response.json()
    result = list(map(lambda x: x['name'], data['results']))
    return result


if __name__ == '__main__':
    data_len = 10
    titles = ['id', 'salary', 'month', 'name']

    ids = generate_ids(data_len)
    salaries = generate_salary(data_len)
    months = generate_month(data_len)
    users = generate_users(data_len)

    data = []
    for i in range(data_len):
        data.append({
            'id': ids[i],
            'salary': salaries[i],
            'month': months[i],
            'name': users[i]['title'] + ' ' + users[i]['first'] + ' ' + users[i]['last']
        })

    write_data('data.csv', data)

    salaries_int = list(map(int, salaries))
    avg_salary = sum(salaries_int) / len(salaries_int)
    print("Средняя зарплата: ", avg_salary)
