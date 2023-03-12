import time
from funcs import RandomArray
from funcs import SelectionSort
#Generate Random numbers
arr = RandomArray(30000)

#Take starting and ending index to apply selection sort
start = int(input("Enter starting index "))
end = int(input("Enter ending index "))

#save starting time
start_time = time.time() 

#call selection sort function
Arr = SelectionSort(arr,start,end)

#save ending time
end_time = time.time() 

#to send the sorted portion to file
s = (Arr[start:end:1])
file = open("SortedSelectionSort.csv",mode = "w")
for i in s:
    file.write(str(i)+"\n")
    
# print the whole array    
print(Arr)
# calculate run time of selection function
run_time = end_time - start_time 

#print run time of function
print("Runtime of selection sort in seconds is  ",run_time,"seconds")