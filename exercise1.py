def simple_calc():
    try:
        x = float(input('Введите выработку часов сотрудника: '))
        y = float(input('Введите ставку за 1 час: '))
        z = float(input('Введите размер премии: '))
        zarplata = (x * y) + z
        return zarplata
    except ValueError:
        return 'Требуется ввести число, а не строку символов'


zp = simple_calc()
if zp == 'Требуется ввести число, а не строку символов':
    print('Требуется ввести число, а не строку символов')
else:
    print(f'Размер заработной платы сотрудника равен: {zp} р.')
