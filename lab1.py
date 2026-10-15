#Импортируем библиотеки
import os
import time

#Вводим константы
BLACK = "\033[40m"
WHITE = "\033[47m"
RED = "\033[41m"
BLUE = "\033[44m"
RESET = "\033[0m"

#ФЛАГ

print(RED + " " * 10 + RESET)
print(WHITE + " " * 10 + RESET)
print(BLUE + " " * 10 + RESET)

#УЗОР

width = 10
height = 13

for y in range(height):
    for x in range(72):
        x = x % 8
        
        left = abs(abs(x - 3) == abs(y - 6)) #Левая диагональ

        right = abs(abs(x - 4) == abs(y - 6)) #Правая диагональ

        if left or right:
            print(BLACK + "  ", end="")
        else:
            print(WHITE + "  ", end="")

    print(RESET)
    
#АНИМАЦИЯ

#Вводим массив, содержащий кадры анимации
frames = [
    "@       ",
    "  @     ",
    "    @   ",
    "      @ "
] 

for frame in frames:
    os.system("cls") #Убираем предыдущий кадр

    print("\033[3;5H", end="") #3;5 - координаты курсора
    print(frame, flush=True)

    time.sleep(0.5) 

#ДИАГРАММА


#Читаем файл
with open("sequence.txt") as file:
    a = file.read().split()
    print(type(a[0]))
    numbers = list(map(float, file.read().split()))

#Суммы 
chet_sum = 0
nechet_sum = 0

#Перебираем числа и их позиции
for i, number in enumerate(numbers, start=1):
    if i % 2 == 0:
        chet_sum += abs(number)
    else:
        nechet_sum += abs(number)

#Общ сумма
total = chet_sum + nechet_sum

if total == 0:
    print("Невозможно вычислить проценты")
else:
    #Вычисляем проценты
    chet_percent = chet_sum / total * 100
    nechet_percent = nechet_sum / total * 100
    
    #Рисуем диаграмму
    width = 50

    chet_width = round(chet_percent / 100 * width)
    nechet_width = width - chet_width

    print(
        BLUE + " " * chet_width +
        RED + " " * nechet_width +
        RESET
    )
    
    test_string = f'{BLUE}{" "*chet_width}{RESET}'

    print("Синий — чётные")
    print("Красный — нечётные")
