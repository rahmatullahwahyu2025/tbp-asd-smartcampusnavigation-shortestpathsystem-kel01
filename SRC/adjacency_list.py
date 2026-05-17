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

# =====================================================================
# CONTOH INPUT UNTUK MENJALANKAN GRAPH
# =====================================================================
if __name__ == "__main__":
    # 1. Membuat objek Graph
    peta_jawa = Graph()

    # 2. Menambahkan Node (node_id, nama_kota)
    peta_jawa.add_node("JKT", "Jakarta")
    peta_jawa.add_node("BDG", "Bandung")
    peta_jawa.add_node("YOG", "Yogyakarta")
    peta_jawa.add_node("SUB", "Surabaya")

    # 3. Menambahkan Edge/Hubungan antar kota beserta bobotnya (misal: jarak dalam km)
    # Karena ini Undirected Graph, hubungan otomatis berlaku bolak-balik
    peta_jawa.add_edge("JKT", "BDG", 150)   # Jakarta <-> Bandung
    peta_jawa.add_edge("JKT", "YOG", 550)   # Jakarta <-> Yogyakarta
    peta_jawa.add_edge("BDG", "YOG", 400)   # Bandung <-> Yogyakarta
    peta_jawa.add_edge("YOG", "SUB", 320)   # Yogyakarta <-> Surabaya

    # 4. Melakukan Cek Tetangga (Neighbors) dari masing-masing kota
    print("=== DAFTAR KOTA DAN TETANGGANYA ===\n")
    
    list_kota = ["JKT", "BDG", "YOG", "SUB"]
    
    for kota_id in list_kota:
        nama_asal = peta_jawa.node_names[kota_id]
        print(f"Kota: {nama_asal} ({kota_id})")
        
        # Mengambil semua tetangga dari kota_id
        daftar_tetangga = peta_jawa.neighbors(kota_id)
        
        if not daftar_tetangga:
            print("  (Tidak memiliki jalur ke kota lain)")
        else:
            for tetangga_id, bobot in daftar_tetangga:
                nama_tetangga = peta_jawa.node_names[tetangga_id]
                print(f"  -> Terhubung ke: {nama_tetangga} ({tetangga_id}) | Jarak: {bobot} km")
        print("-" * 50)
