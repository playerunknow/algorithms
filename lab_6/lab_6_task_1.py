

class Graph:
    def __init__(self, num_vertices):
        # Ініціалізуємо матрицю суміжності нулями
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        # Додаємо орієнтоване ребро (дугу) з вершини src у вершину dest
        if src < self.num_vertices and dest < self.num_vertices:
            self.adj_matrix[src][dest] = 1

    def remove_edge(self, src, dest):
        # Видаляємо ребро з вершини src у вершину dest
        if src < self.num_vertices and dest < self.num_vertices:
            self.adj_matrix[src][dest] = 0

    def display(self):
        # Виводимо матрицю суміжності
        for row in self.adj_matrix:
            print(row)


# Приклад використання
graph = Graph(5)  # Створюємо граф із 5 вершинами
graph.add_edge(0, 1)  # Додаємо дугу з вершини 0 до вершини 1
graph.add_edge(1, 2)  # Додаємо дугу з вершини 1 до вершини 2
graph.add_edge(3, 4)  # Додаємо дугу з вершини 3 до вершини 4
graph.display()  # Виводимо матрицю суміжності
