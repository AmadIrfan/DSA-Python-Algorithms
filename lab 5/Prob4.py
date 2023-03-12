
from Funcs import Sort4

Arr = []
fil=open('data4.txt',mode='r')
lines=fil.read()
arr=lines.split(',')

for i in arr:
    Arr.append(int(i))


array=Sort4(Arr)
print(array)
