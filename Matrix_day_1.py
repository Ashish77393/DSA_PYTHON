def printMatrix(mat):
    # n=len(mat)
    # for i in range(n):
    #     for j in range(n):
    #         print(mat[i][j],end=" ")
    #     print("")

    #print upper triangle,lower triangle,diagonal,left diogonal 
    # n=len(mat)
    # for i in range(n):
    #     for j in range(n):
    #         if j+i==2:#j>=i,j<=i,j==i
    #             print(mat[i][j],end=" ")
    #         else:
    #             print("*",end=" ")
    #     print("")

    # Transpose of matrix 
    n=len(mat)
    print("matrix is : ")
    for i in range(n):
      for j in range(len(mat[0])):
           print(mat[i][j],end=" ")
      print("")
    print("Transpose of matrix is : ")
    rows=len(mat)
    cols=len(mat[0])
    result=[[0]*rows for _ in range(cols)]
    for i in range(rows):
         for j in range(cols):
              result[j][i]=mat[i][j]
    return result
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(printMatrix(mat))