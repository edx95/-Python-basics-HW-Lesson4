# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(f'Числа без повторений: {[el for el in my_list if my_list.count(el) == 1]}')

#v2
'''first = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
second = [el for el in first if first.count(el) == 1]
print(f'Исходный список {first}')
print(f'Итоговый список {second}')'''
