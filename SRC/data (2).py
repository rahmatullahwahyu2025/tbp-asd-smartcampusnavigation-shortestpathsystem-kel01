import random
from typing import List, Tuple

# Set seed global bawaan Python
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