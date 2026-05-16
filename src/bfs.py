from typing import List
from data_structures import QueueLL

def bfs(graph: Graph, source: str) -> List[str]:
    visited = set([source])
    result = []
    queue = QueueLL()
    
    if source in graph.adj:
        queue.enqueue(source)

    while not queue.is_empty():
        u = queue.dequeue()
        result.append(u)
        for v, _ in graph.neighbors(u):
            if v not in visited:
                visited.add(v)
                queue.enqueue(v)
    return result
