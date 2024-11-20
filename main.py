from array import *

def maxone(arr,arr_size):
    counter = 0
    maxONE = 0
    for i in range(0,arr_size):
        if (arr[i] == 0):
            counter = 0
        else:
            counter += 1
            maxONE = max(counter,maxONE) 
    return maxONE           

arr = array("i", [1,0,0,1,1,1,1,1,0,0,1,1,])

#print(maxone(arr,len(arr)))




def pushzerostoend(arr,arr_size):
    zero = 0
    none_zero = 0
    while  (none_zero != arr_size):
          if (arr[none_zero] != 0):
              arr[none_zero], arr[zero] = arr[zero], arr[none_zero]
              zero += 1
          none_zero += 1

check = array("i", [12,0,34,0,0,2,45,0,0])     

pushzerostoend(check,len(check))

print(check)