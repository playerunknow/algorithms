

class Graph:
    def __init__(self, num_vertices):
        # Ініціалізуємо список списків для кожної вершини
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        # Додаємо орієнтоване ребро (дугу) з вершини src до вершини dest
        if src < self.num_vertices and dest < self.num_vertices:
            self.adj_list[src].append(dest)

    def dfs_util(self, vertex, visited):
        # Позначаємо поточну вершину як відвідану
        visited[vertex] = True
        print(vertex, end=" ")

        # Проходимо всіх сусідів вершини
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        # Ініціалізуємо список для відстеження відвіданих вершин
        visited = [False] * self.num_vertices
        # Запускаємо DFS з початкової вершини
        self.dfs_util(start_vertex, visited)


# Приклад використання
graph = Graph(5)  # Створюємо граф із 5 вершинами
graph.add_edge(0, 1)  # Додаємо дугу з вершини 0 до вершини 1
graph.add_edge(0, 2)  # Додаємо дугу з вершини 0 до вершини 2
graph.add_edge(1, 3)  # Додаємо дугу з вершини 1 до вершини 3
graph.add_edge(1, 4)  # Додаємо дугу з вершини 1 до вершини 4
graph.add_edge(3, 4)  # Додаємо дугу з вершини 3 до вершини 4

# Викликаємо обхід у глибину, починаючи з вершини 0
print("Обхід графа у глибину починаючи з вершини 0:")
graph.dfs(0)
