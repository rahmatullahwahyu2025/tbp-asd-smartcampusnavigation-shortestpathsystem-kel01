import random
import time
from dataclasses import dataclass
from typing import Optional, Dict, List, Tuple

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

# --- Fungsi Generate Jalur Otomatis ---
def generate_edges(nodes, seed=7):
    random.seed(seed)
    n = len(nodes)
    edges = []
    indices = list(range(n))
    random.shuffle(indices)
    
    for i in range(1, n):
        u = nodes[indices[i-1]][0]
        v = nodes[indices[i]][0]
        w = random.randint(50, 500)
        edges.append((u, v, w))
    
    extra = int(n * 0.8) 
    for _ in range(extra):
        i, j = random.sample(range(n), 2)
        w = random.randint(50, 500)
        edges.append((nodes[i][0], nodes[j][0], w))
    return edges

# --- Struktur Data Linked List (Queue & Stack) ---
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.head = self.tail = None
    def enqueue(self, data):
        new_node = NodeLL(data)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    def dequeue(self):
        if not self.head: return None
        temp = self.head
        self.head = self.head.next
        if not self.head: self.tail = None
        return temp.data
    def is_empty(self):
        return self.head is None

class StackLL:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = NodeLL(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if not self.top: return None
        temp = self.top
        self.top = self.top.next
        return temp.data
    def is_empty(self):
        return self.top is None

# --- Struktur Data Graph ---
class EdgeNode:
    def __init__(self, dest: str, bobot: int):
        self.dest = dest
        self.bobot = bobot
        self.next: Optional['EdgeNode'] = None

class Graph:
    def __init__(self):
        self.adj: Dict[str, Optional[EdgeNode]] = {}
        self.node_names: Dict[str, str] = {}

    def add_node(self, node_id: str, nama: str):
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.node_names[node_id] = nama

    def add_edge(self, u: str, v: str, bobot: int):
        nv = EdgeNode(v, bobot)
        nv.next = self.adj[u]
        self.adj[u] = nv
        nu = EdgeNode(u, bobot)
        nu.next = self.adj[v]
        self.adj[v] = nu

# --- Algoritma Dijkstra (Pencari Rute Terpendek) ---
def dijkstra(graph: Graph, source: str):
    INF = float('inf')
    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}
    visited = set()
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
        curr = graph.adj[u]
        while curr:
            if dist[u] + curr.bobot < dist[curr.dest]:
                dist[curr.dest] = dist[u] + curr.bobot
                parent[curr.dest] = u
            curr = curr.next
    return dist, parent

def reconstruct_path(parent, source, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == source: break
        curr = parent[curr]
    return path[::-1] if path and path[-1] == source else []

# --- Struktur Data BST (Direktori Gedung) ---
class BSTNode:
    def __init__(self, key, nama):
        self.key, self.nama = key, nama
        self.left = self.right = None

class BSTGedung:
    def __init__(self):
        self.root = None
    def insert(self, key, nama):
        if not self.root: self.root = BSTNode(key, nama); return
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left: curr = curr.left
                else: curr.left = BSTNode(key, nama); break
            elif key > curr.key:
                if curr.right: curr = curr.right
                else: curr.right = BSTNode(key, nama); break
            else: break
    def search(self, key):
        curr = self.root
        while curr:
            if key == curr.key: return curr.nama
            curr = curr.left if key < curr.key else curr.right
        return None

# --- FUNGSI UTAMA (MAIN) ---
def main():
    g = Graph()
    bst = BSTGedung()
    
    # Inisialisasi Data
    for gid, gname in GEDUNG_DATA:
        g.add_node(gid, gname)
        bst.insert(gid, gname)
    
    edges = generate_edges(GEDUNG_DATA, seed=7)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    print("="*60)
    print("        SMART CAMPUS NAVIGATION SYSTEM (VERSI FINAL)")
    print("="*60)
    print("Silakan masukkan perintah (contoh: JALUR A1 C1) atau ketik KELUAR.")
    
    # CLI Loop
    while True:
        try:
            line = input("\n> ").strip().split()
            if not line: continue
            cmd = line[0].upper()

            # --- FITUR MENCARI RUTE MANUAL ---
            if cmd == "JALUR" and len(line) == 3:
                asal = line[1].upper()
                tujuan = line[2].upper()
                
                # Cek apakah gedung terdaftar di memori
                nama_asal = bst.search(asal)
                nama_tujuan = bst.search(tujuan)
                
                if not nama_asal or not nama_tujuan:
                    print("Gagal: ID Gedung tidak ditemukan. Cek lagi kodenya (contoh: A1, B2).")
                    continue
                
                # Menjalankan GPS Dijkstra
                print(f"Mencari rute: {nama_asal} -> {nama_tujuan}...")
                dist, parent = dijkstra(g, asal)
                jalur = reconstruct_path(parent, asal, tujuan)
                
                if jalur:
                    print(f"Rute Terbaik : {' -> '.join(jalur)}")
                    print(f"Total Jarak  : {dist[tujuan]} Meter")
                else:
                    print(f"Jalur terputus. Tidak ada jalan ke {tujuan}.")
            
            elif cmd == "TAMBAH_GEDUNG" and len(line) >= 3:
                gid, gname = line[1], " ".join(line[2:])
                g.add_node(gid, gname); bst.insert(gid, gname)
                print(f"Gedung {gid} ({gname}) berhasil didaftarkan ke sistem.")
            
            elif cmd == "TAMBAH_JALAN" and len(line) == 4:
                u, v, w = line[1].upper(), line[2].upper(), int(line[3])
                g.add_edge(u, v, w)
                print(f"Jalan baru {u}-{v} dengan jarak {w}m telah ditambahkan.")
            
            elif cmd == "KELUAR":
                print("Sistem dimatikan. Sampai jumpa!"); break
            
            else:
                print("Perintah tidak dikenal atau format salah. Silakan coba lagi (contoh: JALUR A1 B2) atau ketik KELUAR.")
        
        except ValueError:
            print("Error: Pastikan format jarak jalan menggunakan angka.")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram dihentikan secara paksa.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan input: {e}")

if __name__ == "__main__":
    main()
