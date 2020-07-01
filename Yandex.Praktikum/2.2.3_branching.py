import random  # импорт объекта random, у которого есть метод randint

current_hour = random.randint(0, 23) # метод randint генерирует случайное целое число в заданном диапазоне

if  current_hour < 12: # напишите условие здесь
    print('Доброе утро!')