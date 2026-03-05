from collections import deque

def DetectCycle(vertices, edges):
    adj_list = [[] for _ in range(vertices)]
    
    # Build adjacency list
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = [0] * vertices
    queue = deque()
    
    queue.append((0, -1))   # (node, parent)
    visited[0] = 1
    print(adj_list)
    while queue:
        node, parent = queue.popleft()
        
        for adjnode in adj_list[node]:
            if visited[adjnode] == 0:
                visited[adjnode] = 1
                queue.append((adjnode, node))
            elif adjnode != parent:
                return True   # Cycle found
    
    return False


edges = [[0,1],[0,2],[1,2],[2,3]]
vertices = 4
print(DetectCycle(vertices, edges))