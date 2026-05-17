from typing import Optional, Dict, List, Tuple

# 1. Definisikan EdgeNode langsung di sini agar tidak ketergantungan file luar
class EdgeNode:
    def __init__(self, dest: str, bobot: int):
        self.dest: str = dest
        self.bobot: int = bobot
        self.next: Optional['EdgeNode'] = None  # Pointer ke node selanjutnya

class Graph:
    def __init__(self):
        # Menyimpan head dari linked list untuk setiap node
        self.adj: Dict[str, Optional[EdgeNode]] = {}
        # Menyimpan representasi nama dari node_id
        self.node_names: Dict[str, str] = {}

    def add_node(self, node_id: str, nama: str) -> None:
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.node_names[node_id] = nama

    def add_edge(self, u: str, v: str, bobot: int) -> None:
        # Memastikan kedua node sudah terdaftar di graph
        if u in self.adj and v in self.adj:
            # Tambah edge dari u ke v
            nv = EdgeNode(v, bobot)
            nv.next = self.adj[u]
            self.adj[u] = nv
            
            # Tambah edge dari v ke u (karena ini Undirected Graph)
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
