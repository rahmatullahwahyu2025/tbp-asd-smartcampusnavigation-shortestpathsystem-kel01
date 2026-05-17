from typing import Optional, List

class BSTNode:
    def __init__(self, key: str, nama: str):
        self.key = key
        self.nama = nama
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BSTGedung:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    # 1. Menambahkan nama fungsi 'insert' yang sempat hilang
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
                    break  # Menambahkan break agar tidak infinite loop
                curr = curr.right  # Menambahkan pergeseran node ke kanan
            else:
                curr.nama = nama
                break

    def search(self, key: str) -> Optional[str]:
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return curr.nama
            elif key < curr.key:
                curr = curr.left   # Diperbaiki: Jika lebih kecil, cari ke kiri (left)
            else:
                curr = curr.right  # Diperbaiki: Jika lebih besar, cari ke kanan (right)
        return None

    def inorder(self) -> List[str]:
        result = []
        
        # Diperbaiki: Mengganti kurung kurawal '}' menjadi ")"
        def _inorder(node: Optional[BSTNode]):
            if node:
                _inorder(node.left)
                result.append(f"{node.key}-{node.nama}")
                _inorder(node.right)
                
        # Diperbaiki: Indentasi pemanggilan fungsi dan return
        _inorder(self.root)
        return result



if __name__ == "__main__":
    bst = BSTGedung()
    
    # Masukkan data
    bst.insert("GD03", "Gedung Rektorat")
    bst.insert("GD01", "Gedung Filkom")
    bst.insert("GD05", "Gedung Teknik")
    
    # Uji Pencarian (Search)
    print("=== Hasil Pencarian ===")
    print("Cari GD01:", bst.search("GD01"))
    print("Cari GD04:", bst.search("GD04")) # Harusnya None karena tidak ada
    
    print("\n=== Hasil Inorder Traversal ===")
    # Uji Cetak Berurutan (Inorder)
    print(bst.inorder())