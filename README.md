# Конфигурационное управление
Вариант №30 <br/>
Задание №3 <br/>
Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. 
Синтаксические ошибки выявляются с выдачей сообщений.  <br/>
Входной текст на языке yaml принимается из стандартного ввода. Выходной текст на учебном конфигурационном языке попадает в стандартный вывод. <br/>
Однострочные комментарии:<br/>
*> Это однострочный комментарий  <br/>
Многострочные комментарии: <br/>
--[[  <br/>
Это многострочный комментарий <br/>
]] <br/>
Массивы: <br/>
'( значение значение значение ... ) <br/>
Имена: <br/> 
[a-z][a-z0-9_]* <br/>
Значения: <br/>
• Числа. <br/>
• Строки. <br/>
• Массивы. <br/>
Строки: <br/>
"Это строка"<br/>
Объявление константы на этапе трансляции: <br/>
def имя = значение; <br/>
Вычисление константного выражения на этапе трансляции (префиксная форма), пример: <br/>
^{+ имя 1} <br/>
Результатом вычисления константного выражения является значение. <br/>
Для константных вычислений определены операции и функции: <br/>
1. Сложение. <br/>
2. Вычитание.<br/>
3. Умножение.<br/>
4. Деление.<br/>
5. concat().<br/>
Дополнительно добавить словарь: '[ значение : ключ ;]<br/>
Все конструкции учебного конфигурационного языка (с учетом их возможной вложенности) должны быть покрыты тестами. Необходимо показать 3 примера
описания конфигураций из разных предметных областей. <br/>
***

## 1. Общее описание<br/>
Этот инструмент командной строки предназначен для преобразования входного текста в формате YAML в выходной текст на учебном конфигурационном языке. 
Программа распознает синтаксические элементы, такие как словари, массивы, строки, числа, комментарии (однострочные и многострочные), а также константы и их вычисления в префиксной форме. В случае 
ошибок синтаксиса программа выдает соответствующие сообщения. <br/>  
## 2. Описание всех функций и настроек <br/> 
**Основные функции:** <br/> 
1. `compute_expression(expression)` <br/> 
Вычисляет значение константного выражения в префиксной форме.<br/> 
Поддерживаемые операции:<br/> 
  -   + — Сложение чисел.<br/> 
  -   - — Вычитание.<br/> 
  -   * — Умножение.<br/> 
  -   / — Деление (с проверкой на деление на 0).<br/> 
  -   concat() — Конкатенация строк.<br/> 
Пример: ^{+ 3 2} вернет 5.<br/> 
2. `process_dict(d)`<br/>
Преобразует словари из формата YAML в формат '[ ключ : значение; ] <br/>
Пример: {a: 1, b: 2} → '[ a : 1; b : 2; ]
3. `process_list(lst)`<br/>
Преобразует списки из YAML в формат '( значение значение значение ... ).<br/>
4. `process_value(value)`<br/>
Определяет тип значения и вызывает соответствующую функцию для обработки:<br/> 
Строки: обрабатывает числа, строки, а также константные выражения.<br/>
Числа: возвращает в формате без кавычек.<br/>
Списки: вызывает process_list.<br/>
Словари: вызывает process_dict.<br/>
6. `generate_config(yaml_input)`<br/>
Основная функция для генерации текста на учебном конфигурационном языке из словаря YAML.<br/>
Распознает комментарии, объявления констант и другие элементы.<br/>
Основные настройки:<br/>
Поддерживаются однострочные комментарии (*>) и многострочные комментарии (--[[ ]]).<br/>
Константы объявляются через def имя = значение;.<br/>
Константные выражения вычисляются с использованием синтаксиса ^{операция аргумент1 аргумент2}.<br/>
Поддерживаемые типы данных: строки, числа, массивы, словари.<br/>
## 3. Описание команд для сборки и запуска проекта <br/>
1. Подготовка проекта<br/>
Перед сборкой убедитесь, что установлены необходимые зависимости.<br/>
Убедитесь, что у вас установлен Python 3.7+<br/>
Установите модуль PyYAML, если он еще не установлен.<br/>
2. Сборка проекта<br/>
Проект написан на Python, и для него не требуется явная компиляция. Вы можете запустить его
напрямую с помощью интерпретатора Python.<br/>
4. Запуск проекта<br/>
Для запуска скрипта выполните следующую команду:<br/>
```
python config_to_yaml.py
```

## 4. Примеры использования <br/>
Примеры вычисления константных выражений (Область: Математическая обработка данных)
![Снимок экрана 2024-12-18 045738](https://github.com/user-attachments/assets/4d727ed7-e875-498b-a9b6-e5d2f569953e)
Пример спортивных соревнований (Область: Организация мероприятий)
![Снимок экрана 2024-12-18 043956](https://github.com/user-attachments/assets/a72d0e2e-ae88-4aef-b9c1-5a6ce7a6c0aa)
Конфиграция веб-сервира (Область: Разработка программного обеспечения)
![Снимок экрана 2024-12-18 043551](https://github.com/user-attachments/assets/b7b7699c-f1b1-412b-8194-405d5954f605)
Конфигурация игры "Плюс Сити" (Область: Разработка игр)
![image](https://github.com/user-attachments/assets/1b17afa1-98bc-46a0-9fc2-d83162af9abe)
## 5. Результаты тестирования<br/>
C:\Users\Taisi\PycharmProjects\ConfigDZ3\.venv\Scripts\python.exe "D:/PyCharm Community Edition 2024.3/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --path C:\Users\Taisi\PycharmProjects\ConfigDZ3\test.py 
Testing started at 0:08 ...
Launching unittests with arguments python -m unittest C:\Users\Taisi\PycharmProjects\ConfigDZ3\test.py in C:\Users\Taisi\PycharmProjects\ConfigDZ3

Ran 11 tests in 0.006s

OK

Process finished with exit code 0

![image](https://github.com/user-attachments/assets/377ebafa-d9d3-4a3e-8079-e976a0cbce99)
