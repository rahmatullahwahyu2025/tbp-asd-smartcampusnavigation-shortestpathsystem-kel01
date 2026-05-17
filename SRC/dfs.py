from typing import List

# =====================================================================
# 1. Implementasi Stack Menggunakan Linked List (StackLL)
# =====================================================================
class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data: str):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("Pop dari stack yang kosong")
        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self) -> bool:
        return self.top is None


# =====================================================================
# 2. Implementasi Graph (Menyesuaikan dengan kebutuhan kode DFS-mu)
# =====================================================================
class Graph:
    def __init__(self):
        # Menggunakan dictionary untuk adjacency list
        self.adj = {}

    def add_edge(self, u: str, v: str, weight: int = 0):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        # Disimpan sebagai tuple (tetangga, bobot) karena kodemu melakukan unpacking (v, _)
        self.adj[u].append((v, weight))

    def neighbors(self, u: str):
        return self.adj.get(u, [])


# =====================================================================
# 3. Fungsi DFS yang Kamu Buat (Sudah Bisa Berjalan)
# =====================================================================
def dfs(graph: Graph, source: str) -> List[str]:
    visited = set()
    result = []
    stack = StackLL()
    
    if source in graph.adj:
        stack.push(source)

    while not stack.is_empty():
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            result.append(u)
            # v = nama simpul tetangga, _ = mengabaikan nilai bobot
            for v, _ in graph.neighbors(u):
                if v not in visited:
                    stack.push(v)
    return result


