import random

array=[]
for  i in range(0,123):
    num=random.randint(0,123)
    array.append(num)
# print(array)

def InsertionSort(arr,start,end):
    for i in range(start,end):
        key=arr[i]
        j=i-1
        while (j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    print(arr)
InsertionSort(array,0,len(array))