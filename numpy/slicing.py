import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
arr1=arr[1:6:2]
print(arr1)
#print their index
for i in range(len(arr1)):
    print(i,arr1[i])
# print the different
print(arr[:5:2])
print(arr[0:7:1])
#arr[start:stop:step]
#question for slicing reverse the array
arr5=arr[: :-1]
print(arr5)