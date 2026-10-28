import heapq

def dijkstra(graph, start, goal):
    # Priority queue stores (current_distance, current_node, path)
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        (cost, current, path) = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if current == goal:
            return path, cost
            
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
                
    return None, float('inf')