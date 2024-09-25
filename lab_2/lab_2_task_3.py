class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Вказівник на наступний елемент
        self.prev = None  # Вказівник на попередній елемент

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Початок списку
        self.tail = None  # Кінець списку

    # Додавання елемента в кінець списку
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # Якщо список порожній
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Виведення списку
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    # Пошук мінімального елементу
    def find_min(self):
        if self.head is None:  # Якщо список порожній
            return None
        min_value = self.head.data
        current = self.head.next
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

# Приклад використання:
dll = DoublyLinkedList()
dll.append(10)
dll.append(3)
dll.append(15)
dll.append(7)

print("Список:")
dll.display()

min_value = dll.find_min()
print(f"Мінімальний елемент у списку: {min_value}")
