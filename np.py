#1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.

import numpy as np

np_ar1 = np.random.random((10,1))
print("array :\n",np_ar1)
m = np.mean(np_ar1)
print("mean of elements:",m)
print("\n")
print("*"*25)
print("\n")

#2-Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.

import numpy as np

np_ar2 = np.random.random((20,1))
print("array :\n",np_ar2)
sd = np.std(np_ar2)
print("STANDARD DEVIATION of elements:",sd)
v = np.var(np_ar2)
print("VARIANCE of elements:",v)
print("\n")
print("*"*25)
print("\n")

#3-Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

import numpy as np

arr_A = np.random.random((10,20))
arr_B = np.random.random((20,25))

print("MATRIX MULTIPLICATION")
arr_C = np.matmul(arr_A,arr_B)
print(arr_C)

s = np.sum(arr_C)
print("SUM OF ELEMENTS:",s)
print("\n")
print("*"*25)
print("\n")

#4-Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A. 

#f(x)=1 / (1 + exp(-x)) 
#Apply this function to each element of A and print the new array holding the value the function returns

import numpy as np
import math

ar_A = np.random.random((10,1))
print("array:\n",ar_A,"\n")

def fun(x):
    #return(x*2)
    return(1 / (1 + math.exp(-x)))

ar_B = np.array((list(map(fun,ar_A))))
print("After mapping:\n",ar_B)
print("\n")
print("*"*25)
print("\n")





    
    


