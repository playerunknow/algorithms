

class Graph:
    def __init__(self, num_vertices):
        # Ініціалізуємо список списків для кожної вершини
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        # Додаємо орієнтоване ребро (дугу) з вершини src до вершини dest
        if src < self.num_vertices and dest < self.num_vertices:
            self.adj_list[src].append(dest)

    def remove_edge(self, src, dest):
        # Видаляємо дугу з вершини src до вершини dest, якщо така є
        if src < self.num_vertices and dest in self.adj_list[src]:
            self.adj_list[src].remove(dest)

    def display(self):
        # Виводимо списки суміжних вершин
        for vertex in range(self.num_vertices):
            print(f"Вершина {vertex}: {self.adj_list[vertex]}")


# Приклад використання
graph = Graph(5)  # Створюємо граф із 5 вершинами
graph.add_edge(0, 1)  # Додаємо дугу з вершини 0 до вершини 1
graph.add_edge(1, 2)  # Додаємо дугу з вершини 1 до вершини 2
graph.add_edge(3, 4)  # Додаємо дугу з вершини 3 до вершини 4
graph.display()  # Виводимо списки суміжних вершин
