from typing import Optional

class NodeLL:
    def __init__(self, data: str):
        self.data = data
        self.next: Optional['NodeLL'] = None

class EdgeNode:
    def __init__(self, dest: str, bobot: int):
        self.dest = dest
        self.bobot = bobot
        self.next: Optional['EdgeNode'] = None
