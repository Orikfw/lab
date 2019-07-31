import numpy as np 

def print_abs_odd():
    """Функція виведення на екран модуля всіх непарних чисел від заданого до 100
       Допускається ввід лице цілих чисел.
    """
    try:
        number = int(input('Введіть ціле початкове число: \n'))
        print('Результат:')
        for numb in range(number, 100):
            if numb % 2 != 0:
                print(abs(numb))
        print('Кінець!')
    except ValueError:
        print('Ви ввели не ціле число!')
        print_abs_odd()


def sum_member_sequence():
    """Функція обчислення суми членів послідовності.
       cos(pi*n)/(n^3)+1
    """
    try:
        sum = 0
        numb = int(input('Введіть ціле число n: \n'))
        for n in range(1, numb + 1):
            numerator = np.cos(np.pi * n)
            denominator = (n**3) + 1
            sum += numerator / denominator
        print(f'Сума членів послідовності: {sum}')
    except ValueError:
        print('Ви ввели не ціле число!')
        sum_member_sequence()
        

def table_cubes_numb():
    """Функція створює таблицю кубів для чисел від 20 до 30 з кроком 0.3"""
    print('Вихідне число: \t Куб вихідного числа:')
    for numb in np.arange(20, 30, 0.3):
        cube_numb = numb ** 3
        print('{0:.3f} \t\t'.format(numb) + ' {0:.3f}'.format(cube_numb))
    

def table_sm_ft():
    """Функція створює таблицю відповідності між футами і сантиметрами для значень від 1 
    до 100 футів з кроком 1 фут (1 фут = 30.48 сантиметра)
    """
    print('Фути: \t Сантиметри:')
    for feet in range(1, 101):
        centimeter = feet * 30.48
        print(feet, '\t {0:.2f}'.format(centimeter))


def solve():
    """Функція обчислює значення a i b за заданих x, y, z
    Швидше за все працює не правильно..
    """
    try:
        x = float(input('Введіть x: '))
        y = float(input('Введіть y: '))
        z = float(input('Введіть z: '))
        a_numerator = y + 1 / (np.power(x, 2) + 1)
        a_denominator = np.exp(-2 + np.cos(z)) + (3 + x * y ** 4) ** (-4)
        a = a_numerator / a_denominator
        b_numerator = 1 + np.sin(2 - x)
        b_denominator = 4 + y ** 4 / 4 + np.tan(z) ** 2
        b = b_numerator / b_denominator
        print(f'А: {a}')
        print(f'B: {b}')
    except ValueError:
        print('Ви ввели щось не те')
        solve()