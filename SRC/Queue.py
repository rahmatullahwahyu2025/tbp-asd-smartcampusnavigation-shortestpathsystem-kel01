from typing import Optional

# Dependensi Node yang dibutuhkan oleh Queue
class NodeLL:
    def __init__(self, data: str):
        self.data = data
        self.next: Optional['NodeLL'] = None

class QueueLL:
    def __init__(self):
        self.head: Optional[NodeLL] = None
        self.tail: Optional[NodeLL] = None
        
    def enqueue(self, data: str):
        new_node = NodeLL(data)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
    def dequeue(self) -> Optional[str]:
        if not self.head: 
            return None
        temp = self.head
        self.head = self.head.next
        if not self.head: 
            self.tail = None
        return temp.data
        
    def is_empty(self) -> bool:
        return self.head is None
