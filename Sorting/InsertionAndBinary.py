def swap(arr,i,j) :
    arr[i],arr[j] = arr[j],arr[i]
    

def binsearch(arr,key,low = 0,high = None) :
    if high == None : high = len(arr) - 1
    if low > high : return low
    
    mid = (low + high) // 2

    if (key == arr[mid]) : return mid
    elif(key > arr[mid]) : return binsearch(arr,key,mid + 1,high)
    return binsearch(arr,key,low,mid - 1)
    
    
def InsertionSort(arr,i = 0,j = 0) :
    if i == len(arr) : return arr
    j = i
    v = arr[i]
    pos = binsearch(arr, v, 0, i - 1)
    while j > pos:
        arr[j] = arr[j - 1]
        j -= 1
    arr[j] = v
    
    return InsertionSort(arr,i + 1)