import time
import random  # Імпортуємо модуль для генерації випадкових чисел

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Время выполнения {func.__name__}: {execution_time:.4f} секунд")
        return result
    return wrapper

# Пример использования декоратора
@timeit
def example_function():
    # Ваш код здесь
    time.sleep(1)  # Имитация долгой работы

example_function()


@timeit
def generate_random_array(n, lower_bound=0, upper_bound=100):
    """
    Генерує випадковий масив із n елементів у діапазоні від lower_bound до upper_bound.

    :param n: кількість елементів у масиві
    :param lower_bound: нижня межа для генерації чисел (включно)
    :param upper_bound: верхня межа для генерації чисел (включно)
    :return: список із випадковими числами
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]


generate_random_array(10000)


