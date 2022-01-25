def binary_search(list, item):
    # Задаем начальные условия для поиска
    # low - это минимальное значение индекса в списке list
    # high - это максимальное значение индекса в списке list

    low = 0
    high = len(list)-1

    while low <= high:
        # Целочисленное деление максимального индекса на минимальный, чтобы получить среднее значение
        middle = (low + high)//2
        # Проверяем является ли среднее значение списка значением которое мы ищем
        if list[middle] == item:
            return middle
        # Если средний элемент больше искомого элемента, то максимальное значение становится middle - 1
        # и мы "отсекаем" верхнюю половину списка
        if list[middle] > item:
            high = middle - 1
        # Если средний элемент меньше искомого элемента, то минимальное значение становится middle + 1
        # и мы "отсекаем" нижнюю половину списка
        else:
            low = middle + 1
    # Если в процессе выполнения бинарного поиска индекс искомого элемента не был найден, то возвращаем None
    return None

my_list_for_search = [1,2,3,4,5,67,78,99,100,134,135,169,266,299,341]

print(binary_search(my_list_for_search, 134)) # Будет выведен индекс 9. Вспомните: нумерация элементов начинается с 0.
print(binary_search(my_list_for_search, 137)) # Будет выведено None
