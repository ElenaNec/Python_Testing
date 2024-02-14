# Задание 3
# На вход в качестве аргументов программы поступают три пути к файлу (в приложении
# к заданию находятся примеры этих файлов):
# ● values.json содержит результаты прохождения тестов с уникальными id
# ● tests.json содержит структуру для построения отчета на основе прошедших
# тестов (вложенность может быть большей, чем в примере)
# ● report.json - сюда записывается результат.
# Напишите программу, которая формирует файл report.json с заполненными полями
# value для структуры tests.json на основании values.json.
# Структура report.json такая же, как у tests.json, только заполнены поля “value”.
# На вход программы передается три пути к файлу!

import json
import sys

def update_report_with_values(values_path, tests_path, report_path):
    # Загрузка данных из файлов
    try:
        with open(values_path, 'r') as values_file:
            values_data = json.load(values_file)
    except FileNotFoundError:
        print(f"File {values_path} not found.")
        sys.exit(1)

    try:
        with open(tests_path, 'r') as tests_file:
            tests_data = json.load(tests_file)
    except FileNotFoundError:
        print(f"File {tests_path} not found.")
        sys.exit(1)

    # Функция для обновления значений в тестах
    def update_values(tests, values):
        for test_item in tests:
            test_id = test_item.get('id')
            test_item['value'] = next((value['value'] for value in values if value['id'] == test_id), "")
            if 'values' in test_item:
                update_values(test_item['values'], values)

    update_values(tests_data['tests'], values_data['values'])

    # Запись обновленных данных в файл report.json
    with open(report_path, 'w') as report_file:
        json.dump(tests_data, report_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Use the format: python task3.py values_path tests_path report_path")
        sys.exit(1)

    values_path = sys.argv[1]  # values.json
    tests_path = sys.argv[2]   # tests.json
    report_path = sys.argv[3]  # report.json

    update_report_with_values(values_path, tests_path, report_path)
