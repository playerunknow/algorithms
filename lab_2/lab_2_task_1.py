
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Queue is now empty
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def find_min(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        min_value = self.queue[self.front]
        index = self.front
        while True:
            if self.queue[index] < min_value:
                min_value = self.queue[index]
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        return min_value

    def remove_min(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        min_value = self.find_min()
        index = self.front
        min_index = -1

        # Find index of the minimum value
        while True:
            if self.queue[index] == min_value:
                min_index = index
                break
            if index == self.rear:
                break
            index = (index + 1) % self.capacity

        # Remove the minimum value
        for i in range(min_index, (self.rear + 1) % self.capacity):
            next_index = (i + 1) % self.capacity
            if next_index == self.front:
                break
            self.queue[i] = self.queue[next_index]

        self.rear = (self.rear - 1) % self.capacity
        if self.rear == -1:
            self.front = -1  # Queue is now empty
        return min_value

# Приклад використання
cq = CircularQueue(5)
cq.enqueue(5)
cq.enqueue(1)
cq.enqueue(3)
cq.enqueue(4)

print("Мінімальний елемент:", cq.find_min())  # Виведе: Мінімальний елемент: 1
print("Видалений мінімальний елемент:", cq.remove_min())  # Виведе: Видалений мінімальний елемент: 1
print("Мінімальний елемент після видалення:", cq.find_min())  # Виведе: Мінімальний елемент після видалення: 3

