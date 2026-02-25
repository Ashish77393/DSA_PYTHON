from collections import deque
def Orange(mat):
    n=len(mat)
    fresh_fruit=0
    queue=deque()
    for i in range(0,n):
        for j in range(0,n):
            if mat[i][j]==2:
                queue.append((i,j))
            if mat[i][j]==1:
                fresh_fruit+=1
    min=0
    rotten=len(queue.popleft())
    for _ in range(rotten):
        i,j=queue.popleft()
        top=[i-1][j]
        bottom=[i+1,j]
        left=[i,j-1]
        right=[i,j+1]
        if mat[top]==1:
            mat[top]=2
            

    


mat=[[2,1,1],[1,1,0],[0,1,1]]
print(Orange(mat))