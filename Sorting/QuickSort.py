def swap(arr,i,j) :
    arr[i],arr[j] = arr[j],arr[i]
    
def quickSort(arr,low, high ) :
    if(low < high) :
        s = partition(arr,low, high )
        quickSort(arr,low,s-1)
        quickSort(arr,s+1,high)
        
def partition(arr,low, high ) :
    i=low
    j= high + 1
    pivot = arr[low]
    
    while True :
        while True :
            i+=1
            if i >= high or pivot < arr[i] : break
        while True :
            j-=1
            if j <= low  or pivot > arr[j] : break

        swap(arr,i,j)
        if i >= j : break
    swap(arr,i,j)
    swap(arr,low,j)
    
    return j
    
