

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Кількість вершин
        self.edges = []           # Список ребер (u, v, вага)

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def get_edges(self):
        # Повертає всі ребра, відсортовані за вагою (для Краскала)
        return sorted(self.edges)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Стиснення шляху
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph):
    mst = []  # Список для зберігання ребер мінімального остового дерева (МОД)
    uf = UnionFind(graph.vertices)

    # Сортуємо ребра за вагою
    edges = graph.get_edges()

    for weight, u, v in edges:
        # Якщо вершини u і v не належать одній компоненті, додамо ребро в MST
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst

# Приклад використання
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = kruskal(g)

# Виведення результату
print("Мінімальне остове дерево:")
total_weight = 0
for u, v, weight in mst:
    print(f"Ребро {u}-{v} з вагою {weight}")
    total_weight += weight

print(f"Загальна вартість мінімального остового дерева: {total_weight}")
