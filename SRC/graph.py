from typing import Optional, Dict, List, Tuple

# =====================================================================
# 1. IMPLEMENTASI STRUKTUR DATA PENDUKUNG (data_structures)
# =====================================================================

class EdgeNode:
    """Node untuk melambangkan edge dalam adjacency list graph berbobot."""
    def __init__(self, dest: str, bobot: int):
        self.dest: str = dest
        self.bobot: int = bobot
        self.next: Optional['EdgeNode'] = None


class QueueNode:
    def __init__(self, data: str):
        self.data: str = data
        self.next: Optional['QueueNode'] = None

class QueueLL:
    """Queue menggunakan Linked List untuk menunjang algoritma BFS."""
    def __init__(self):
        self.front: Optional[QueueNode] = None
        self.rear: Optional[QueueNode] = None

    def enqueue(self, data: str) -> None:
        new_node = QueueNode(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self) -> str:
        if self.is_empty():
            raise IndexError("Dequeue dari queue yang kosong")
        temp = self.front
        self.front = temp.next # type: ignore
        if self.front is None:
            self.rear = None
        return temp.data # type: ignore

    def is_empty(self) -> bool:
        return self.front is None


class StackNode:
    def __init__(self, data: str):
        self.data: str = data
        self.next: Optional['StackNode'] = None

class StackLL:
    """Stack menggunakan Linked List untuk menunjang algoritma DFS."""
    def __init__(self):
        self.top: Optional[StackNode] = None

    def push(self, data: str) -> None:
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("Pop dari stack yang kosong")
        popped = self.top.data # type: ignore
        self.top = self.top.next # type: ignore
        return popped

    def is_empty(self) -> bool:
        return self.top is None


# =====================================================================
# 2. STRUKTUR DATA GRAPH & ALGORITMA (Kode Asli Kamu)
# =====================================================================

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

def dijkstra(graph: Graph, source: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    INF = float('inf')
    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}
    visited = set()
    
    if source not in graph.adj:
        return dist, parent
        
    dist[source] = 0

    for _ in range(len(graph.adj)):
        u = None
        min_dist = INF
        for v in graph.adj:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
                
        if u is None: break
        visited.add(u)
        
        for v, weight in graph.neighbors(u):
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    
    return dist, parent

def reconstruct_path(parent: Dict[str, Optional[str]], source: str, target: str) -> List[str]:
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == source: break
        curr = parent.get(curr)
    return path[::-1] if path and path[-1] == source else []

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
            for v, _ in graph.neighbors(u):
                if v not in visited:
                    stack.push(v)
    return result


