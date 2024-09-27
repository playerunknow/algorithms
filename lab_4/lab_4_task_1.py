

class BitSet:
    def __init__(self, max_size):
        # Максимальний розмір множини
        self.max_size = max_size
        # Використовуємо ціле число як бітовий вектор
        self.set = 0

    def add(self, element):
        if 0 <= element < self.max_size:
            # Установка відповідного біта в 1
            self.set |= (1 << element)
        else:
            raise ValueError(f"Element {element} is out of bounds.")

    def remove(self, element):
        if 0 <= element < self.max_size:
            # Скидання відповідного біта в 0
            self.set &= ~(1 << element)
        else:
            raise ValueError(f"Element {element} is out of bounds.")

    def contains(self, element):
        if 0 <= element < self.max_size:
            # Перевірка відповідного біта
            return (self.set & (1 << element)) != 0
        else:
            raise ValueError(f"Element {element} is out of bounds.")

    def union(self, other):
        if self.max_size != other.max_size:
            raise ValueError("Sets must have the same max size.")
        # Об'єднання множин (побітове OR)
        result = BitSet(self.max_size)
        result.set = self.set | other.set
        return result

    def intersection(self, other):
        if self.max_size != other.max_size:
            raise ValueError("Sets must have the same max size.")
        # Перетин множин (побітове AND)
        result = BitSet(self.max_size)
        result.set = self.set & other.set
        return result

    def difference(self, other):
        if self.max_size != other.max_size:
            raise ValueError("Sets must have the same max size.")
        # Різниця множин (побітове AND з доповненням)
        result = BitSet(self.max_size)
        result.set = self.set & ~other.set
        return result

    def __str__(self):
        # Повертає множину у вигляді списку
        return "{" + ", ".join(str(i) for i in range(self.max_size) if self.contains(i)) + "}"

# Приклад використання
bit_set1 = BitSet(10)
bit_set2 = BitSet(10)

bit_set1.add(1)
bit_set1.add(3)
bit_set1.add(5)

bit_set2.add(3)
bit_set2.add(4)
bit_set2.add(5)

print("Множина 1:", bit_set1)
print("Множина 2:", bit_set2)

union_set = bit_set1.union(bit_set2)
print("Об'єднання:", union_set)

intersection_set = bit_set1.intersection(bit_set2)
print("Перетин:", intersection_set)

difference_set = bit_set1.difference(bit_set2)
print("Різниця:", difference_set)
