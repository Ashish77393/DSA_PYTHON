def MatrixRotate90(mat):
    n=len(mat)
    # result=[[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(len(mat[0])):
    #         result[j][(n-1)-i]=mat[i][j]
    # return result


    #optimal solutions
    for i in range(n-1):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    for i in range(len(mat)):
        mat[i].reverse()
    return mat
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(MatrixRotate90(mat))