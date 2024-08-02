import json
import sys


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def fill_values(tests_structure, values_data):
    def recursive_fill(test):
        # Если это обычный тест с id, обновляем значение
        if 'id' in test:
            test['value'] = values_data.get(test['id'], None)

        # Если это структура с вложенными тестами
        if 'tests' in test:
            for sub_test in test['tests']:
                recursive_fill(sub_test)

    # Начинаем рекурсивную обработку с корневого элемента
    recursive_fill(tests_structure)
    return tests_structure


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main(values_path, tests_path, report_path):
    # Загружаем данные из файлов
    values_data = load_json(values_path)
    tests_structure = load_json(tests_path)

    # Заполняем значения
    filled_report = fill_values(tests_structure, values_data)

    # Сохраняем результат в файл
    save_json(report_path, filled_report)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)