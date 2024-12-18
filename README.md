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
Все конструкции учебного конфигурационного языка (с учетом их возможной вложенности) должны быть покрыты тестами. Необходимо показать 3 примера описания конфигураций из разных предметных областей. <br/>
***

## 1. Общее описание<br/>
## 2. Описание всех функций и настроек <br/> 
## 3. Описание команд для сборки проекта.<br/>
## 4. Примеры использования 
## 5. Результаты тестирования<br/>
C:\Users\Taisi\PycharmProjects\ConfigDZ3\.venv\Scripts\python.exe "D:/PyCharm Community Edition 2024.3/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py" --path C:\Users\Taisi\PycharmProjects\ConfigDZ3\test.py 
Testing started at 3:02 ...
Launching unittests with arguments python -m unittest C:\Users\Taisi\PycharmProjects\ConfigDZ3\test.py in C:\Users\Taisi\PycharmProjects\ConfigDZ3

Ran 9 tests in 0.005s

OK

Process finished with exit code 0
![image](https://github.com/user-attachments/assets/fe0daaba-9ebd-41cc-8cb7-2f9fc61f0e9e)

