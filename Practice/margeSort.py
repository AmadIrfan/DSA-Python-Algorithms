from random import randint

array=[]

for i in range(0,10):
    num=randint(0,10)
    array.append(num)
    

def Merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q
    left=[]
    right=[]

def MergeSort(arr,p,r):
    if (p!=r):
        q=(p+r)//2
        MergeSort(arr,p,q)
        MergeSort(arr,q+1,r)
        Merge(arr,p,q,r)


p=0
r=len(array)
MergeSort(array,p,r)