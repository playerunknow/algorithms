
class Node:
    def __init__(self, value):
        self.value = value  # Значення слова
        self.weight = 0     # Вага слова
        self.left = None    # Лівий підвузол
        self.right = None   # Правий підвузол


class WeightedTree:
    def __init__(self):
        self.root = None

    def insert(self, value, weight):
        if self.root is None:
            self.root = Node(value)
            self.root.weight = weight
        else:
            self._insert_recursive(self.root, value, weight)

    def _insert_recursive(self, node, value, weight):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.weight = weight
            else:
                self._insert_recursive(node.left, value, weight)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                node.right.weight = weight
            else:
                self._insert_recursive(node.right, value, weight)
        else:
            # Якщо значення вже існує, оновлюємо вагу
            node.weight = weight

    def find_next(self, value):
        return self._find_next_recursive(self.root, value)

    def _find_next_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            left_result = self._find_next_recursive(node.left, value)
            return left_result if left_result is not None else node.value

        return self._find_next_recursive(node.right, value)

# Приклад використання
tree = WeightedTree()
tree.insert("apple", 1)
tree.insert("banana", 2)
tree.insert("cherry", 3)

next_word = tree.find_next("apple")
print("Наступне слово після 'apple':", next_word)

next_word = tree.find_next("banana")
print("Наступне слово після 'banana':", next_word)

next_word = tree.find_next("cherry")
print("Наступне слово після 'cherry':", next_word)
