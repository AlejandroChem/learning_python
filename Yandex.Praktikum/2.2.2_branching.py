import random  # импорт объекта random, у которого есть метод randint

messages_count = random.randint(0, 5) # метод randint генерирует случайное целое число в заданном диапазоне

# напишите ваш код здесь
if messages_count > 0:
    print('Новых сообщений:', str(messages_count))
else:
    print('У вас нет новых сообщений')