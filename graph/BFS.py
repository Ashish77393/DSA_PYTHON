from collections import deque
def BFS(n,adj,start):
    ans=[]
    queue=deque()
    visited_arr=[0]*(n+1)
    queue.append(start)
    visited_arr[start]=1
    while len(queue)!=0:
        e=queue.popleft()
        ans.append(e)
        for node in adj[e]:
            if visited_arr[node]==0:
                queue.append(node)
                visited_arr[node]=1
    return ans
n=9
adj=[
[],
[2,8],
[1,3,4],
[2],
[2,5],
[4,6],
[5,7],
[6,8],
[1,7,9],
[8],
]
print(BFS(n,adj,1))