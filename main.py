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
# algorithms.py
import random

def generate_edges(nodes, seed=7):
    """Menghasilkan jalur (edges) acak antar gedung."""
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

def dijkstra(graph, source: str):
    """Algoritma Dijkstra untuk mencari jarak dan rute terpendek."""
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
    """Merekontruksi jalur dari node asal ke tujuan."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == source: break
        curr = parent[curr]
    return path[::-1] if path and path[-1] == source else []
