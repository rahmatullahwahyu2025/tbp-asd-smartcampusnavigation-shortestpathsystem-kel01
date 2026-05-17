import random
from typing import Optional, Dict, List, Tuple


random.seed(7)

# --- Data gedung (30 node simulatif) ---
GEDUNG_DATA = [
    ('A1', 'Gerbang Utama'), ('A2', 'Rektorat'),
    ('B1', 'FIB'),    ('B2', 'FT'),
    ('B3', 'Lab Elektronika'), ('B4', 'Lab Komputer'),
    ('C1', 'FMIPA'),  ('C2', 'Perpustakaan'),
    ('D1', 'Stadion'),         ('D2', 'GOR'),
    ('E1', 'FK'), ('E2', 'FIKK'),
    ('F1', 'FEB'), ('F2', 'Kantin Pusat'),
    ('G1', 'FISIP'),    ('G2', 'Masjid Kampus'),
    ('H1', 'Pascasarjana'),    ('H2', 'Auditorium'),
    ('I1', 'Lab Bahasa'),      ('I2', 'FBSB'),
    ('J1', 'GYM'),    ('J2', 'Kantin'),
    ('K1', 'Student Center'),  ('K2', 'Koperasi'),
    ('L1', 'Stadion L'),     ('L2', 'Security Post'),
    ('M1', 'Gedung Alumni'),   ('M2', 'Museum Pendidikan'),
    ('N1', 'Bakso Pajero'),   ('N2', 'Tempat Parkir')
]

def generate_edges(nodes: List[Tuple[str, str]], seed: int = 7) -> List[Tuple[str, str, int]]:
    random.seed(seed)
    n = len(nodes)
    edges = []
    
    perm = list(range(n))
    random.shuffle(perm)
    
    for i in range(1, n):
        u = nodes[perm[i-1]][0]
        v = nodes[perm[i]][0]
        w = random.randint(50, 500)  
        edges.append((u, v, w))
        
    extra = int(n * 0.5)
    for _ in range(extra):
        i, j = random.sample(range(n), 2)
        w = random.randint(50, 500)
        edges.append((nodes[i][0], nodes[j][0], w))
        
    return edges



class BSTNode:
    def __init__(self, key: str, nama: str):
        self.key = key
        self.nama = nama
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BSTGedung:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: str, nama: str) -> None:
        if self.root is None:
            self.root = BSTNode(key, nama)
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = BSTNode(key, nama)
                    break
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = BSTNode(key, nama)
                    break 
                curr = curr.right  
            else:
                curr.nama = nama
                break

    def search(self, key: str) -> Optional[str]:
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return curr.nama
            elif key < curr.key:
                curr = curr.left   
            else:
                curr = curr.right  
        return None

    def inorder(self) -> List[str]:
        result = []
        
        def _inorder(node: Optional[BSTNode]):
            if node:
                _inorder(node.left)
                result.append(f"{node.key}-{node.nama}")
                _inorder(node.right)
                
        _inorder(self.root)
        return result



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



def main():
    g = Graph()
    bst = BSTGedung()
    
    # Inisialisasi data
    for gid, gname in GEDUNG_DATA:
        g.add_node(gid, gname)
        bst.insert(gid, gname)
        
    edges = generate_edges(GEDUNG_DATA, seed=7)
    for u, v, w in edges:
        g.add_edge(u, v, w)
        
    print("="*60)
    print("Smart Campus Navigation System")
    print("Ketik BANTUAN untuk daftar perintah")
    print("="*60)
    
    while True:
        try:
            cmd_input = input("\n> ").strip().split()
            if not cmd_input: continue
            
            cmd = cmd_input[0].upper()
            args = cmd_input[1:]
            
            if cmd == "BANTUAN":
                print("Daftar Perintah:")
                print("  TAMBAH_GEDUNG <id> <nama>")
                print("  TAMBAH_JALAN <u> <v> <jarak>")
                print("  JALUR <asal> <tujuan>")
                print("  JELAJAH_BFS <sumber>")
                print("  JELAJAH_DFS <sumber>")
                print("  CARI_GEDUNG <kode>")
                print("  TERISOLASI")
                print("  LAPORAN_GRAPH")
                print("  KELUAR")
                
            elif cmd == "CARI_GEDUNG":
                if len(args) == 1:
                    hasil = bst.search(args[0])
                    print(f"Hasil: {hasil}" if hasil else "Gedung tidak ditemukan.")
                else: print("Format: CARI_GEDUNG <kode>")
                
            elif cmd == "JALUR":
                if len(args) == 2:
                    asal, tujuan = args[0], args[1]
                    dist, parent = dijkstra(g, asal)
                    path = reconstruct_path(parent, asal, tujuan)
                    
                    if path:
                        print(f"Jarak total: {dist[tujuan]} meter")
                        rute = [f"{n}({g.node_names[n]})" for n in path]
                        print("Rute: " + " -> ".join(rute))
                    else:
                        print(f"Tidak ada jalur dari {asal} ke {tujuan}.")
                else: print("Format: JALUR <asal> <tujuan>")

            elif cmd == "JELAJAH_BFS":
                if len(args) == 1:
                    rute = bfs(g, args[0])
                    print("BFS:", " -> ".join(rute))
                else: print("Format: JELAJAH_BFS <sumber>")

            elif cmd == "JELAJAH_DFS":
                if len(args) == 1:
                    rute = dfs(g, args[0])
                    print("DFS:", " -> ".join(rute))
                else: print("Format: JELAJAH_DFS <sumber>")

            elif cmd == "TAMBAH_GEDUNG":
                if len(args) >= 2:
                    gid, gname = args[0], " ".join(args[1:])
                    g.add_node(gid, gname)
                    bst.insert(gid, gname)
                    print(f"Gedung {gid} ditambahkan.")
                else: print("Format: TAMBAH_GEDUNG <id> <nama>")

            elif cmd == "TAMBAH_JALAN":
                if len(args) == 3:
                    g.add_edge(args[0], args[1], int(args[2]))
                    print(f"Jalan {args[0]}-{args[1]} ditambahkan.")
                else: print("Format: TAMBAH_JALAN <u> <v> <jarak>")

            elif cmd == "TERISOLASI":
                terjangkau = set(bfs(g, 'A1'))
                semua_gedung = set(g.adj.keys())
                terisolasi = semua_gedung - terjangkau
                if terisolasi:
                    print(f"Gedung Terisolasi: {', '.join(terisolasi)}")
                else:
                    print("Semua gedung terhubung ke jaringan utama (A1).")

            elif cmd == "LAPORAN_GRAPH":
                print(f"Total Gedung (Node): {len(g.adj)}")
                total_edge = sum(len(g.neighbors(u)) for u in g.adj) // 2
                print(f"Total Jalan (Edge): {total_edge}")

            elif cmd == "KELUAR":
                print("Sistem dihentikan.")
                break
                
            else:
                print("Perintah tidak dikenali. Ketik BANTUAN.")
                
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == '__main__':
    main()
