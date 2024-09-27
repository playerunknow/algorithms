

class ArrayTree:
    def __init__(self):
        # Дерево зберігається у вигляді списку
        self.tree = []

    def add(self, value):
        """Додає новий елемент у дерево"""
        self.tree.append(value)

    def find_left_to_right(self, value):
        """Пошук зліва направо (обхід in-order для бінарного дерева)"""
        for i in range(len(self.tree)):
            if self.tree[i] == value:
                return f"Елемент {value} знайдено на позиції {i}."
        return f"Елемент {value} не знайдено."

    def find_top_to_bottom(self, value):
        """Пошук зверху вниз (обхід рівнями, breadth-first search)"""
        queue = [0]  # Починаємо з кореня дерева
        while queue:
            idx = queue.pop(0)
            if idx < len(self.tree):
                if self.tree[idx] == value:
                    return f"Елемент {value} знайдено на позиції {idx}."
                # Додаємо лівого та правого нащадка до черги
                left_child = 2 * idx + 1
                right_child = 2 * idx + 2
                queue.append(left_child)
                queue.append(right_child)
        return f"Елемент {value} не знайдено."

    def find_bottom_to_top(self, value):
        """Пошук знизу вгору (обхід пост-ордер для бінарного дерева)"""
        for i in range(len(self.tree)-1, -1, -1):
            if self.tree[i] == value:
                return f"Елемент {value} знайдено на позиції {i}."
        return f"Елемент {value} не знайдено."

# Приклад використання
tree = ArrayTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)

print(tree.find_left_to_right(5))  # Пошук зліва направо
print(tree.find_top_to_bottom(3))  # Пошук зверху вниз
print(tree.find_bottom_to_top(4))  # Пошук знизу вгору
