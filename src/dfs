from typing import List
from data_structures import StackLL

def dfs(graph: Graph, source: str) -> List[str]:
    visited = set()
    result = []
    stack = StackLL()
    
    if source in graph.adj:
        stack.push(source)

    while not stack.is_empty():
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            result.append(u)
            for v, _ in graph.neighbors(u):
                if v not in visited:
                    stack.push(v)
    return result
