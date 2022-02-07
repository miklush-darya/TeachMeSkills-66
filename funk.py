
year_y = int(input('введите год: '))

month_m = int(input('введите месяц: '))
if month_m > 12:
    print('месяц введен не верно, введите новое значение: ')
    month_m = int(input())

day_d = int(input('введите день: '))
if day_d > 31:
    print('день введен не верно, введите новое значение до 31: ')
    day_d = int(input())

if month_m %2 == 0 and month_m < 8:
    if day_d > 30:
        print('день введен не верно, введите новое значение до 30: ')
        day_d = int(input())

if month_m %2 != 0 and month_m >=8 and month_m<=12:
    if day_d > 30:
        print('день введен не верно, введите новое значение до 30: ')
        day_d = int(input())

if year_y % 4 == 0 and month_m == 2 and day_d > 30:
    print('день введен не верно, введите новое значение: ')
    day_d = int(input())

if month_m == 2 and day_d > 29:
    print('день введен не верно, введите новое значение: ')
    day_d = int(input())



data_d = f'{year_y}-{month_m}-{day_d}'
print(data_d)
