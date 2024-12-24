# Домашнее задание по теме "Списковые, словарные сборки"

# Задача:
# Даны несколько списков, состоящих из строк
# first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
# second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
# 1 В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
#   при условии, что длина строк не менее 5 символов.
# 2 В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей)
#   одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
# 3 В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-
#   - длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
#   Условие записи пары в словарь - чётная длина строки.

# Примечания:
# Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
print(first_result)
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
print(second_result)
# a = first_strings.extend(second_strings)
third_result = {string: len(string) for string in (first_strings + second_strings) if not len(string) % 2}
print(third_result)