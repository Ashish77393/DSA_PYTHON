def DFS(adj,start,n):
    ans=[0]*(n+1)
    result=[]
    stack=[start]
    while stack:
        e=stack.pop()
        if ans[e]==0:
            ans[e]=1
            result.append(e)
            for neighbour in reversed(adj[e]):
                if ans[neighbour]==0:
                    stack.append(neighbour)
    return result
n=9
adj=[

    [],
    [2,4],
    [1,3,6],
    [2],
    [1,5,7],
    [4,8],
    [2],
    [4,8],
    [5,7]
]
start=1
print(DFS(adj,start,n))


