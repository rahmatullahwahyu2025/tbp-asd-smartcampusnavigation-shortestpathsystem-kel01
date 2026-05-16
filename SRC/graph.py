from typing import Optional, Dict, List, Tuple
from data_structures import QueueLL, StackLL

# --- Node untuk Linked List adjacency list ------------------------------------
class EdgeNode:
    def __init__(self, dest: str, bobot: int):
        self.dest = dest
        self.bobot = bobot
        self.next: Optional['EdgeNode'] = None

# --- Graph --------------------------------------------------------------------
class Graph:
    def __init__(self):
        self.adj: Dict[str, Optional[EdgeNode]] = {}
        self.node_names: Dict[str, str] = {}

    def add_node(self, node_id: str, nama: str) -> None:
        """Big-O: O(1)."""
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.node_names[node_id] = nama

    def add_edge(self, u: str, v: str, bobot: int) -> None:
        """Big-O: O(1) tambah di head linked list. (graf tidak berarah)"""
        if u in self.adj and v in self.adj:
            nv = EdgeNode(v, bobot)
            nv.next = self.adj[u]
            self.adj[u] = nv
            
            nu = EdgeNode(u, bobot)
            nu.next = self.adj[v]
            self.adj[v] = nu

    def neighbors(self, u: str) -> List[Tuple[str, int]]:
        """Big-O: O(deg(u))."""
        res = []
        curr = self.adj.get(u)
        while curr:
            res.append((curr.dest, curr.bobot))
            curr = curr.next
        return res

# --- Algoritma Rute & Eksplorasi ----------------------------------------------
def dijkstra(graph: Graph, source: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    """Big-O: O(V^2 + E) dengan array sederhana."""
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
        # Cari node dengan jarak terkecil yang belum dikunjungi
        for v in graph.adj:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
                
        if u is None: break
        visited.add(u)
        
        # Update tetangga
        for v, weight in graph.neighbors(u):
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    
    return dist, parent

def reconstruct_path(parent: Dict[str, Optional[str]], source: str, target: str) -> List[str]:
    """Rekonstruksi jalur dari parent dict. Big-O: O(V)."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == source: break
        curr = parent.get(curr)
    return path[::-1] if path and path[-1] == source else []

def bfs(graph: Graph, source: str) -> List[str]:
    """BFS berbasis Queue Linked List. Big-O: O(V + E)."""
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
    """DFS berbasis Stack Linked List. Big-O: O(V + E)."""
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
            # Push ke stack (urutan terbalik agar traversal sesuai)
            for v, _ in graph.neighbors(u):
                if v not in visited:
                    stack.push(v)
    return result
