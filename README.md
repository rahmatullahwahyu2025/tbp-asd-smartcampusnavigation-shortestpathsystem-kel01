# 🎓 TBP ASD: Smart Campus Navigation & Shortest Path System

Repositori ini berisi *source code* untuk **Tugas Besar Praktikum Algoritma dan Struktur Data (TBP ASD)** oleh **Kelompok 01**. 

Proyek ini adalah simulasi sistem navigasi kampus cerdas (*Smart Campus Navigation System*) berbasis *Command Line Interface* (CLI). Sistem dibangun sepenuhnya menggunakan bahasa Python dari nol (*from scratch*), mengimplementasikan struktur data tingkat rendah tanpa menggunakan *library* eksternal untuk mendemonstrasikan pemahaman algoritma secara mendalam.

## 👥 Anggota Kelompok 01
| Nama | NIM |
| :--- | :--- |
| **[Maizan Arifin]** | (25051030009) |
| **[Habibi Aulia Rizki]** |   (25051030010) |
| **[Nicholas Candra Pascalis]** | (25051030011) |
| **[Rahmatullah Wahyu Nugroho]** | (25051030038) |
| **[Juan Ramadhani]** | (25051030039) |

  ## 📈 Kompleksitas Algoritma
Modul	Kompleksitas
Add Node	O(1)
Add Edge	O(1)
Neighbors	O(deg(v))
Dijkstra	O(V² + E)
BFS	O(V + E)
DFS	O(V + E)
BST Search	O(log V) rata-rata
Inorder BST	O(V)

## 📂 Struktur Direktori

* `/SRC` - Berisi *source code* utama aplikasi (`main.py` dan implementasi struktur data).
* `/docs` - Berisi dokumentasi proyek, laporan, atau panduan tambahan.
* `/test` & `/tests` - Berisi modul pengujian (*unit testing*) untuk memvalidasi fungsi algoritma.
* `/AI_Log` - Catatan penggunaan atau interaksi AI selama pengembangan.

## ✨ Fitur Utama
* **Pencarian Rute (Shortest Path):** Menemukan jalur terpendek dan jarak total antar gedung menggunakan algoritma Dijkstra.
* **Direktori Cepat:** Mencari nama gedung berdasarkan ID dalam waktu logaritmik menggunakan *Binary Search Tree (BST)*.
* **Eksplorasi Area:** Menelusuri koneksi jaringan jalan kampus menggunakan metode BFS (*Breadth-First Search*) dan DFS (*Depth-First Search*).
* **Deteksi Isolasi:** Mengidentifikasi gedung-gedung yang jalurnya terputus dari jaringan utama kampus.
* **Peta Dinamis:** Menambahkan gedung baru dan menyambungkan jalan secara *real-time* via CLI.

## 💻 Command Line Interface (CLI)
# input
> TERISOLASI
# Output
Semua gedung terhubung ke jaringan utama (A1).
# input
> CARI_GEDUNG B2
# output
Hasil: FT

## 🛠️ Implementasi Struktur Data
Sistem ini dibangun menggunakan struktur data fundamental berikut:
1. **Singly Linked List:** Fondasi dasar untuk antrian (*Queue*), tumpukan (*Stack*), dan *Adjacency List*.
2. **Graph (Adjacency List):** Merepresentasikan peta kampus dengan efisiensi memori $O(V+E)$.
3. **Queue & Stack:** Diimplementasikan manual untuk mendukung operasi BFS dan DFS pada waktu konstan $O(1)$.
4. **Binary Search Tree (BST):** Sebagai sistem basis data untuk pencarian gedung yang sangat cepat.

## 🚀 Cara Menjalankan Program

1. *Clone* repositori ini ke komputer lokal Anda:
   ```bash
   git clone [https://github.com/rahmatullahwahyu2025/tbp-asd-smartcampusnavigation-shortestpathsystem-kel01.git](https://github.com/rahmatullahwahyu2025/tbp-asd-smartcampusnavigation-shortestpathsystem-kel01.git)
