from typing import Optional, Dict, List, Tuple
from data_structures import EdgeNode

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
