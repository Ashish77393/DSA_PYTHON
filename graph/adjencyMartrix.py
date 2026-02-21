n=5
m=6
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
metrix=[[0 for _ in range(n+1)] for _ in range(n+1)]
# print(metrix)
# for e,v in edges:
#     metrix[e][v]=1
#     metrix[v][e]=1
# print(metrix)
# using list
lst=[[] for _ in range(n+1)]
print(lst)
for e,v in edges:
    lst[e].append(v)
    lst[v].append(e)
print(lst)
mydict={}
for i in range(1,n+1):
    mydict[i]=[]
for e,v in edges:
    mydict[e].append(v)
    mydict[v].append(e)
print(mydict)
