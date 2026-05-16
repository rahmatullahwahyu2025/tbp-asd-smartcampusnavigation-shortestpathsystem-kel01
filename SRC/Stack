from typing import Optional

# Dependensi Node yang dibutuhkan oleh Stack
class NodeLL:
    def __init__(self, data: str):
        self.data = data
        self.next: Optional['NodeLL'] = None

class StackLL:
    def __init__(self):
        self.top: Optional[NodeLL] = None
        
    def push(self, data: str):
        new_node = NodeLL(data)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self) -> Optional[str]:
        if not self.top: 
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
        
    def is_empty(self) -> bool:
        return self.top is None
