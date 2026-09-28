import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr1=arr[0:2,0:3]
print(arr1)
#numpy give the index value using special function np.ndenumerate
for index,value in np.ndenumerate(arr1):
    print(index,value)
   # perform the matrix tranpose 
  
arr3 =np.arange(1,10)
print(arr3)
arr3=arr3.reshape(3,3)
print(arr3) 
arr4=np.transpose(arr3)
print(arr4)

#

   

