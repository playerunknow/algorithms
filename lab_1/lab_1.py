# lab_1

import random  # Імпортуємо модуль для генерації випадкових чисел
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"execution_time {func.__name__}: {execution_time:.4f} секунд \n")
        return result
    return wrapper


def generate_random_array(n, lower_bound=0, upper_bound=100):
    """
    Генерує випадковий масив із n елементів у діапазоні від lower_bound до upper_bound.

    :param n: кількість елементів у масиві
    :param lower_bound: нижня межа для генерації чисел (включно)
    :param upper_bound: верхня межа для генерації чисел (включно)
    :return: список із випадковими числами
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]


@timeit
# BubbleSort
def BubbleSort(main_array):
    n = len(main_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if main_array[j] > main_array[j + 1]:
                main_array[j], main_array[j + 1] = main_array[j + 1], main_array[j]


@timeit
# InsertionSort
def InsertionSort(main_array):
    n = len(main_array)
    for i in range(1, n):
        insert_index = i
        current_value = main_array.pop(i)
        for j in range(i - 1, -1, -1):
            if main_array[j] > current_value:
                insert_index = j
        main_array.insert(insert_index, current_value)


# QuickSort

def quicksort(main_array):
    # Якщо масив містить один або менше елементів, він вже відсортований
    if len(main_array) <= 1:
        return main_array

    # Вибираємо опорний елемент (pivot) - середній елемент масиву
    pivot = main_array[len(main_array) // 2]

    # Створюємо три списки:
    # 1. Елементи, що менші за опорний
    left = [x for x in main_array if x < pivot]

    # 2. Елементи, що дорівнюють опорному
    middle = [x for x in main_array if x == pivot]

    # 3. Елементи, що більші за опорний
    right = [x for x in main_array if x > pivot]

    # Рекурсивно сортуємо ліву та праву частини і об'єднуємо всі три частини
    return quicksort(left) + middle + quicksort(right)


# Hoare's QuickSort
def quicksortHoare(main_array, low, high):
    if low < high:
        # Отримати індекс поділу
        pi = partition(main_array, low, high)

        # Рекурсивно сортувати елементи перед і після поділу
        quicksortHoare(main_array, low, pi)
        quicksortHoare(main_array, pi + 1, high)


def partition(main_array, low, high):
    # Вибрати середній елемент як опорний
    pivot = main_array[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        # Шукати елемент більший за опорний
        i += 1
        while main_array[i] < pivot:
            i += 1

        # Шукати елемент менший за опорний
        j -= 1
        while main_array[j] > pivot:
            j -= 1

        # Якщо індекси перетнулися, повернути індекс поділу
        if i >= j:
            return j

        # Якщо ні, поміняти місцями
        main_array[i], main_array[j] = main_array[j], main_array[i]


# Виклик функції для створення масиву з 20 випадкових чисел
random_array1 = generate_random_array(1000, 0, 10000)
random_array2 = generate_random_array(2000, 0, 10000)
random_array3 = generate_random_array(3000, 0, 10000)
random_array4 = generate_random_array(4000, 0, 10000)
random_array5 = generate_random_array(5000, 0, 10000)
random_array6 = generate_random_array(6000, 0, 10000)


def calculation(random_array):

    main_array = random_array[:]
    BubbleSort(main_array)

    main_array = random_array[:]
    InsertionSort(main_array)

    main_array = random_array[:]
    start_time = time.perf_counter()
    quicksort(main_array)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("execution_time quicksort time =", round(execution_time, 4), "\n")

    main_array = random_array[:]
    start_time = time.perf_counter()
    quicksortHoare(main_array, 0, len(main_array) - 1)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("execution_time quicksortHoare =", round(execution_time, 4), "\n")

    print('\n\n\n\n\n\n\n')


calculation(random_array1)
calculation(random_array2)
calculation(random_array3)
calculation(random_array4)
calculation(random_array5)
calculation(random_array6)

