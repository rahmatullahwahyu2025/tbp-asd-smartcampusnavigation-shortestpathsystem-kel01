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
                # Jika key sudah ada, update namanya
                curr.nama = nama
                break

    def search(self, key: str) -> Optional[str]:
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return curr.nama
            elif key < curr.key:
                curr = curr.left   # Ke kiri jika key lebih kecil
            else:
                curr = curr.right  # Ke kanan jika key lebih besar
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

