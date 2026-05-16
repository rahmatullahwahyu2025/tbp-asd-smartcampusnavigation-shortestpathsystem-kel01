from typing import Optional, Dict, List, Tuple

def dijkstra(graph: Graph, source: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    INF = float('inf')
    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}
    visited = set()
    
    if source not in graph.adj:
        return dist, parent
        
    dist[source] = 0

    for _ in range(len(graph.adj)):
        u = None
        min_dist = INF
        for v in graph.adj:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
                
        if u is None: break
        visited.add(u)
        
        for v, weight in graph.neighbors(u):
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    
    return dist, parent

def reconstruct_path(parent: Dict[str, Optional[str]], source: str, target: str) -> List[str]:
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == source: break
        curr = parent.get(curr)
    return path[::-1] if path and path[-1] == source else []
