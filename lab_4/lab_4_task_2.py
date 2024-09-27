

class OrderedSet:
    def __init__(self):
        self._elements = []

    def add(self, element):
        """Додає елемент до множини, якщо його ще немає."""
        if element not in self._elements:
            self._elements.append(element)
            self._elements.sort()  # підтримуємо впорядкованість

    def remove(self, element):
        """Видаляє елемент з множини."""
        if element in self._elements:
            self._elements.remove(element)

    def contains(self, element):
        """Перевіряє, чи містить множина заданий елемент."""
        return element in self._elements

    def size(self):
        """Повертає кількість елементів у множині."""
        return len(self._elements)

    def to_list(self):
        """Повертає список елементів множини."""
        return self._elements.copy()

    def __str__(self):
        """Повертає строкове представлення множини."""
        return "{" + ", ".join(map(str, self._elements)) + "}"

# Приклад використання
if __name__ == "__main__":
    ordered_set = OrderedSet()
    ordered_set.add(5)
    ordered_set.add(3)
    ordered_set.add(8)
    ordered_set.add(5)  # Не буде додано, оскільки 5 вже є

    print(ordered_set)  # Виведе: {3, 5, 8}
    print(ordered_set.contains(3))  # Виведе: True
    print(ordered_set.size())  # Виведе: 3

    ordered_set.remove(3)
    print(ordered_set)  # Виведе: {5, 8}
