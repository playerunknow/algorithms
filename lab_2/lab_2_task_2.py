class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class LinkedListWithStacks:
    def __init__(self):
        self.left_stack = Stack()   # Ліва частина списку
        self.right_stack = Stack()  # Права частина списку

    def add_left(self, value):
        self.left_stack.push(value)

    def add_right(self, value):
        self.right_stack.push(value)

    def move_left(self):
        if not self.right_stack.is_empty():
            self.left_stack.push(self.right_stack.pop())

    def move_right(self):
        if not self.left_stack.is_empty():
            self.right_stack.push(self.left_stack.pop())

    def get_left(self):
        return self.left_stack.peek()

    def get_right(self):
        return self.right_stack.peek()

    def is_empty(self):
        return self.left_stack.is_empty() and self.right_stack.is_empty()

    def size(self):
        return self.left_stack.size() + self.right_stack.size()

    def find_min(self):
        min_value = float('inf')

        # Перевіряємо всі елементи у лівому стеку
        for value in self.left_stack.stack:
            if value < min_value:
                min_value = value

        # Перевіряємо всі елементи у правому стеку
        for value in self.right_stack.stack:
            if value < min_value:
                min_value = value

        return min_value if min_value != float('inf') else None


ll = LinkedListWithStacks()
ll.add_left(10)
ll.add_left(5)
ll.add_right(15)
ll.add_right(3)

print("Мінімальний елемент:", ll.find_min())  # Виведе: Мінімальний елемент: 3
