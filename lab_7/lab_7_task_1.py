

class Graph:
    def __init__(self, vertices):
        # Ініціалізуємо кількість вершин і порожню матрицю суміжності
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Додаємо ребро між вершинами u і v
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # Неорієнтований граф

    def display(self):
        # Виводимо матрицю суміжності
        for row in self.adj_matrix:
            print(row)

# Приклад використання
graph = Graph(5)  # Створюємо граф з 5 вершинами
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 4)

graph.display()
