#Задание 1
# list_type = (1, 2.0, complex(3, 4), '5', True, None)
#
# for el in list_type:
#     print(f'type: {type(el)}')

#Задание 2
# usr_list = []
# while True:
#     usr_value = int(input("Введите значение. Для выход введите '-1': "))
#
#     if usr_value == -1:
#         break
#
#     usr_list.append(usr_value)
#
# cnt = len(usr_list) if len(usr_list) % 2 == 0 else len(usr_list) - 1
#
# print(f'До изменений: {usr_list}')
#
# if cnt != 0:
#     for i in range(0, cnt, 2):
#         usr_list[i], usr_list[i + 1] = usr_list[i + 1], usr_list[i]
#
# print(f'После изменений: {usr_list}')

#Задание 3
# list_month = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
# dict_month = {'1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето',
#               '7': 'Лето', '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима'}
#
# indx_month = int(input('Введите месяц в числовом виде: '))
#
# if indx_month < 1 or indx_month > 12:
#     print(f'Месяц {indx_month} не относится ни к какому времени года')
# else:
#     print(f'Время года из list: {list_month[indx_month - 1]}')
#     print(f'Время года из dict: {dict_month.get(str(indx_month))}')

#Задание 4
# usr_str = input('Введите несколько строк через пробел: ')
#
# for el in usr_str.split(' '):
#     if(len(el) > 10):
#         print(f'{el[0:10]}...')
#     else:
#         print(el)

#Задание 5
from random import randint
import datetime

usr_list = [7, 5, 3, 3, 2]
usr_list2 = [7, 5, 3, 3, 2]
usr_list3 = [7, 5, 3, 3, 2]

max_val = max(usr_list)
min_val = min(usr_list)

def find_indx(value, begin, end):
    global usr_list

    middl = int((begin + end) / 2)

    print(f'{middl + 1} - {usr_list[middl + 1]} : {middl} - {usr_list[middl]} : {middl -1 } - {usr_list[middl - 1]}')

    if usr_list[middl - 1] > value and usr_list[middl] < value:
        return middl + 1
    elif usr_list[middl + 1] < value and usr_list[middl] > value:
        return middl + 1
    else:
        if value > usr_list[middl]:
            return find_indx(value, begin, middl)
        if value < usr_list[middl]:
            return find_indx(value, middl, end)

def ins_alg(value):
    global max_val
    global min_val
    global usr_list

    try:
        usr_list.insert(usr_list.index(value) + 1, value)
    except:
        if max_val < value:
            usr_list.insert(0, value)
            max_val = value
        elif min_val > value:
            usr_list.append(value)
            min_val = value
        else:
            usr_list.insert(find_indx(value, 0, len(usr_list)), value)

while True:
    usr_value = int(input('Введите число! Для прекращения операции введите -1: '))

    if usr_value == -1:
        break;

    ins_alg(usr_value)

print(f'Список: {usr_list}')

#first---------------------------------------------------------------------------------------------
# now_sort1 = datetime.datetime.now()
#
# cnt = 0
#
# print(f'sort in cycle now_sort {now_sort1}')
#
# while True:
#     if cnt == 100000:
#         break
#
#     any_val = randint(0, 100000)
#     usr_list2.append(any_val)
#     usr_list2.sort()
#
#     cnt += 1
#
# then_sort1 = datetime.datetime.now();
#
# print(f'sort in cycle then_sort: {then_sort1}')
#
# delta_sort1 = now_sort1 - then_sort1
#
# print(f"sort in cycle sort time: {delta_sort1.microseconds}")

#-----------------------------------------------------

#second--------------------------------------------------------------------------------------------
# now_sort2 = datetime.datetime.now()
#
# cnt = 0
#
# print(f'sort in after cycle now_sort {now_sort2}')
#
# while True:
#     if cnt == 100000000:
#         break
#
#     any_val = randint(0, 100000000)
#     usr_list3.append(any_val)
#
#     cnt += 1
#
# usr_list3.sort()
#
# then_sort2 = datetime.datetime.now();
#
# print(f'sort in after cycle then_sort: {then_sort2}')
#
# delta_sort2 = now_sort2 - then_sort2
#
# print(f"sort in after cycle sort time: {delta_sort2.microseconds}")

# -----------------------------------------------------

#third---------------------------------------------------------------------------------------------
# now_sort3 = datetime.datetime.now()
#
# cnt = 0
#
# print(f'my example now_sort {now_sort3}')
#
# while True:
#     if cnt == 100000000:
#         break
#
#     any_val = randint(0, 100000000)
#     usr_list.append(any_val)
#
#     cnt += 1
#
# then_sort3 = datetime.datetime.now();
#
# print(f'my example then_sort: {then_sort3}')
#
# delta_sort3 = now_sort3 - then_sort3
#
# print(f"my example sort time: {delta_sort3.microseconds}")

#(100.000)   1. 154650 2. 892135 3. 895715
#(1.000.000) 2. 975360 3. 247196
#(10.000.000) 2. 416370 3. 77110
#(100.000.000) 2.975687 3. 775101