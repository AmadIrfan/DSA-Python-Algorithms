from random import randint
# arr=[]
# for i in range(20):
#     arr.append(randint(0,20),)
# print(arr)

arr=[9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1]
# def insertionSort(arr1,s,e):
#     for i in range(s,e):
#         key=arr1[i]
#         j=i-1
#         while j>=0 and key<arr1[j]:
#             arr1[j+1]=arr1[j]
#             j=j-1
#         arr1[j+1]=key
#     return arr1

def Partition(ar1,p,r):
    pivt=ar1[r]
    i=p-1
    for j in range(p,r):
        if(ar1[j]<=pivt):
            i=i+1
            p1=ar1[i]
            ar1[i]=ar1[j]
            ar1[j]=p1
    p2=ar1[r]
    ar1[r]=ar1[i+1]
    ar1[i+1]=p2
    return i+1
def quickSort(arr1,p,r):
    if(p<r):
        q=Partition(arr1,p,r)
        quickSort(arr1,p,q-1)
        quickSort(arr1,q+1,r)
    return arr1

# def partition(ar1,p,r):
#     pivt=ar1[r]
#     j=p-1
#     i=p
#     for i in range(r-1):
#         if(ar1[i]<pivt):
#             j=j+1
#             tp1=ar1[j]
#             ar1[i]=tp1
#     tp2=ar1[r]
#     ar1[j+1]=tp2
#     return i+1
# def quickSort(arr1,p,r):
#     if p<r:
#         q=Partition(arr1,p,r)
#         quickSort(arr1,p,q-1)
#         quickSort(arr1,q+1,r)
#     print(arr1)
# print(arr)

print(quickSort(arr,0,len(arr)-1))
# def Merge(arr,p,q,r):
#     n1=q-p+1
#     n2=r-q
#     left=[]
#     right=[]
#     for i in range (n1+1):
#         left.append(arr[p+i,-1])
#     for j in range(n2+1):
#         right.append(j+q)

#     left.append(100000),right.append(1000000)

# def MergeSort(arr,p,r):
#     if (p!=r):
#         q=(p+r)//2
#         MergeSort(arr,p,q)
#         MergeSort(arr,q+1,r)
#         Merge(arr,p,q,r)

# print(insertionSort(arr,0,len(arr)))