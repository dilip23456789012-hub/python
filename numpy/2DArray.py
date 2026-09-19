import numpy as np
arr=np.array([[10,20,30],[40,50,60]])
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(i, j, arr[i][j])
