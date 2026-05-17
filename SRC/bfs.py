from typing import Optional, Dict, List, Tuple

# ==========================================
# 1. STRUKTUR DATA UNTUK GRAPH & QUEUE
# ==========================================

class EdgeNode:
    def __init__(self, dest: str, bobot: int):
        self.dest: str = dest
        self.bobot: int = bobot
        self.next: Optional['EdgeNode'] = None

class Graph:
    def __init__(self):
        self.adj: Dict[str, Optional[EdgeNode]] = {}
        self.node_names: Dict[str, str] = {}

    def add_node(self, node_id: str, nama: str) -> None:
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.node_names[node_id] = nama

    def add_edge(self, u: str, v: str, bobot: int) -> None:
        if u in self.adj and v in self.adj:
            nv = EdgeNode(v, bobot)
            nv.next = self.adj[u]
            self.adj[u] = nv
            
            nu = EdgeNode(u, bobot)
            nu.next = self.adj[v]
            self.adj[v] = nu

    def neighbors(self, u: str) -> List[Tuple[str, int]]:
        res = []
        curr = self.adj.get(u)
        while curr:
            res.append((curr.dest, curr.bobot))
            curr = curr.next
        return res

# Implementasi QueueLL (Queue menggunakan Linked List)
class QueueNode:
    def __init__(self, data: str):
        self.data = data
        self.next: Optional['QueueNode'] = None

class QueueLL:
    def __init__(self):
        self.head: Optional[QueueNode] = None
        self.tail: Optional[QueueNode] = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, data: str) -> None:
        new_node = QueueNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self) -> str:
        if self.is_empty():
            raise IndexError("Dequeue dari queue yang kosong")
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.data


# ==========================================
# 2. FUNGSI BFS (KODEMU SUDAH BENAR)
# ==========================================

def bfs(graph: Graph, source: str) -> List[str]:
    visited = set([source])
    result = []
    queue = QueueLL()
    
    if source in graph.adj:
        queue.enqueue(source)

    while not queue.is_empty():
        u = queue.dequeue()
        result.append(u)
        for v, _ in graph.neighbors(u):
            if v not in visited:
                visited.add(v)
                queue.enqueue(v)
    return result


