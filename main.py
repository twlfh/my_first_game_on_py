import random

min_number = 1
max_number = 100
max_attempts = 7

sacred_number = random.randint(min_number, max_number)

message = f'Вітаю! Я загадав число від 1 до 100. У вас є 7 спроб щоб його вгадати.'
print(message)

for attempt in range(1, 8):
    try:
        input_num = int(input('Введіть ваше припущення тут: '))
    except ValueError:
        print('Введіть ціле число!')
        continue
    if input_num < sacred_number:
        print('Ваше число менше ніж те, що я загадав.')
        print(f'\tЗалишилось спроб {max_attempts - attempt}')
    elif input_num > sacred_number:
        print('Ваше число більше ніж те, що я загадав.')
        print(f'\tЗалишилось спроб {max_attempts - attempt}')
    else:
        print('Вітаю, ви вгадали!')
        break
else:
    print(f'Нажаль, спроби закінчились. Загадане мною число: {sacred_number}.')