# def  infinityMatrix(mat,row,columns):
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if i==row or j==columns:
#                 mat[i][j]=float('inf')
# def MatrixSetZero(mat):
#     n=len(mat)
#     m=len(mat[0])
#     for row in range(n):
#         for columns in range(m):
#             if mat[row][columns]==0:
#                 infinityMatrix(mat,row,columns)
#     for row in range(n):
#         for columns in range(m):
#             if mat[row][columns]==float('inf'):
#                 mat[row][columns]=0
#     for row in range(len(mat)):
#         for columns in range(len(mat[0])):
#             print(mat[row][columns],end=" ")
#         print("")


#Second Method And Optimal Solutions 
def MatrixSetZero(mat):
    row=len(mat)
    columns=len(mat[0])
    rowtrack=[0 for _ in range(row)]
    coltrack=[0 for _ in range(columns)]
    for i in range(row):
        for j in range(columns):
            if mat[i][j]==0:
                rowtrack[i]=-1
                coltrack[j]=-1
    for i in range(row):
        for j in range(columns):
            if rowtrack[i]==-1 or coltrack[j]==-1:
                mat[i][j]=0
    return mat
    

mat=[[1,2,0,3],[2,3,4,8],[0,6,7,9],[6,9,5,2]]        
print(MatrixSetZero(mat))