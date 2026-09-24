import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
# print index and all the elements of the array
for i in range(len(arr)):
    print(i,arr[i])
# PRINT THE MATRIX
matrix=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(i,j,matrix[i][j])

#



