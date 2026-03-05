from collections import deque
def ShortestDistance(mat,n):
    queue=deque()
    rows=len(mat)
    cols=len(mat[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    distancematrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if mat[i][j]==0:
                queue.append([i,j,0])
                visited[i][j]=1
    while len(queue)!=0:
        i,j,d=queue.popleft()
        distancematrix[i][j]=d
        for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
            new_i,new_j=i+x,j+y
            if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                continue

            if visited[new_i][new_j]==1:
                continue
            queue.append([new_i,new_j,d+1])
            visited[new_i][new_j]=1
    return distancematrix

mat=[[1,1,1],[1,0,1],[0,1,0]]
n=len(mat)
print(ShortestDistance(mat,n))