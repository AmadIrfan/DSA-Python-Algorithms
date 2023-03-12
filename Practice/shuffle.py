
import random as rand
array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(array)
leArr=len(array)
print(leArr)
for i in range(0,leArr):
    j=rand.randint(0,leArr-1)
    temp=array[i]
    array[j]=array[i]
    array[j]=temp
print(array)