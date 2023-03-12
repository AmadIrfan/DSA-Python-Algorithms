from Funcs import SumIterative 
from Funcs import SumRecursive 

num=input('Enter a Number : ' )

number= SumIterative(int(num))
print ('Iterative Sum',number)
num=SumRecursive(number)
print('Recursive Sum',num)