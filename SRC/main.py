# Import dari file lokal yang telah kita buat
from data import GEDUNG_DATA, generate_edges
from graph import Graph, dijkstra, reconstruct_path, bfs, dfs
from bst import BSTGedung

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
    print("Smart Campus Navigation System (Modular Version)")
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
