# Домашнее задание по теме "Создание функций на лету"

# Задача "Функциональное разнообразие"

# Lambda-функция:
#     Даны 2 строки:
#     first = 'Мама мыла раму'
#     second = 'Рамена мало было'
#     Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
#     Здесь ? - место написания lambda-функции.
#
#     Результатом должен быть список совпадения букв в той же позиции:
#     [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
#     Где True - совпало, False - не совпало.
#
# Замыкание:
#     Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
#     Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
#     неограниченное количество данных любого типа.
#     Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
#     Функция get_advanced_writer возвращает функцию write_everything.
#
#     Данный код:
#     write = get_advanced_writer('example.txt')
#     write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#     Запишет данные в файл в таком виде:

# Метод __call__:
#     Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
#     В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words
#     и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете
#     использовать функцию choice из модуля random.
#
#     Ваш код (количество слов для случайного выбора может быть другое):
#     from random import choice
#     # Ваш класс здесь
#     first_ball = MysticBall('Да', 'Нет', 'Наверное')
#     print(first_ball())
#     print(first_ball())
#     print(first_ball())
#     Примерный результат (может отличаться из-за случайности выбора):
#     Да
#     Да
#     Наверное
#
# Примечания:
# 1 Все задания пишутся в одном модуле.
# 2 Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы ваш код полноценно демонстрировал
#   логику написанного.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result) # Результатом должен быть список совпадения букв в той же позиции, где True - совпало, False - не совпало

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+', encoding='utf-8') as file:
            if hasattr(data_set, "__iter__"): # проверка типа данных *data_set
                file.seek(2)
                for line in data_set:
                    file.write(f'\n{line}')
            else:
                file.write(f'\n{data_set}')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
      return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Не знаю')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())