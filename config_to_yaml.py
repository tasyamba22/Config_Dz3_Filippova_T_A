import sys
import re
import yaml

# Константные операции
def compute_expression(expression):
    #Вычисление константного выражения в префиксной форме.
    #Поддержка операций: +, -, *, /, concat.
    tokens = expression.split()
    if len(tokens) < 3:
        raise ValueError("Некорректное константное выражение")

    operator = tokens[0]
    arguments = tokens[1:]

    if operator in ['+', '-', '*', '/']:
        # Преобразуем аргументы в числа
        try:
            numbers = [float(arg) for arg in arguments]
        except ValueError:
            raise ValueError(f"Ожидались числовые аргументы для операции {operator}")

        # Выполняем вычисления
        if operator == '+':
            return str(sum(numbers))
        elif operator == '-':
            return str(numbers[0] - numbers[1])
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num
            return str(result)
        elif operator == '/':
            if numbers[1] == 0:
                raise ZeroDivisionError("Деление на ноль")
            return str(numbers[0] / numbers[1])
    elif operator == 'concat':
        # Убираем кавычки из аргументов и соединяем
        strings = [re.sub(r"^['\"]|['\"]$", '', arg) for arg in arguments]
        return ''.join(strings)

    else:
        raise ValueError(f"Неизвестная операция: {operator}")

# Обработка словарей
def process_dict(d):
    # Преобразование словаря в формат '[ ключ : значение; ]
    result = "'["
    for key, value in d.items():
        result += f" {key} : {process_value(value)};"
    result += " ]"
    return result

# Обработка массивов
def process_list(lst):
    # Преобразование списка в формат с переносами строк.
    values = ' '.join(process_value(item) for item in lst)
    return f"'( {values} )"

def process_value(value):
    # Преобразование значений в целевой формат
    if isinstance(value, str):
        if re.match(r'^\^\{.*\}$', value):  # Константное выражение
            expression = value[2:-1]
            return compute_expression(expression)
        # Пробуем преобразовать строку в число
        try:
            # Проверка на целое число
            int_value = int(value)
            return str(int_value)  # Возвращаем целое число без точки
        except ValueError:
            try:
                # Проверка на число с плавающей точкой
                float_value = float(value)
                return str(float_value)  # Возвращаем число
            except ValueError:
                return f'"{value}"'  # Если это не число, возвращаем строку в кавычках
    elif isinstance(value, (int, float)):  # Если это число
        # Если это целое число, выводим как целое
        if isinstance(value, int):
            return str(value)
        return str(value)
    elif isinstance(value, list):
        return process_list(value)  # Массив
    elif isinstance(value, dict):
        return process_dict(value)  # Словарь
    else:
        raise ValueError(f"Неизвестное значение: {value}")

# Генерация конфигурации
def generate_config(yaml_input):
    # Генерация выходного текста на учебном конфигурационном языке
    output = ""
    for key, value in yaml_input.items():
        # Проверка имени ключа
        if not re.match(r'^[a-z][a-z0-9_]*', key):
            raise ValueError(f"Некорректное имя ключа: {key}")
        if key.startswith("comment"):  # Однострочные комментарии
            output += f"*> {value}\n"
        elif key.startswith("multicomment"):  # Многострочные комментарии
            output += f"--[[\n{value.strip()}\n]]\n"  # Убираем лишние пробелы
        elif key.startswith("def"):  # Константы
            const_name, const_value = value.split("=", 1)
            const_name = const_name.strip()
            const_value = process_value(const_value.strip())
            output += f"def {const_name} = {const_value};\n"
        else:
            output += f"{key} = {process_value(value)}\n"
    return output

# Чтение ввода с пустой строкой для завершения
def main():
    # Чтение YAML и вывод конфигурации
    print("Введите текст в формате YAML, закончите ввод пустой строкой и нажатием Enter:")

    input_data = ""
    while True:
        line = input()
        # Завершаем ввод, если строка пустая
        if line.strip() == "":
            break
        input_data += line + "\n"

    try:
        # Преобразуем YAML в Python-словарь
        yaml_input = yaml.safe_load(input_data)
        # Генерация выходного текста в формате учебного конфигурационного языка
        result = generate_config(yaml_input)
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()


