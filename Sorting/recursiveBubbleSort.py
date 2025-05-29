def BubbleSort(arr,n,i = 0,j = 0) :
    if i == n - 1 :
        return arr
    
    if j == n - 1 - i : 
        return BubbleSort(arr,n,i + 1,0)
        
    if (arr[j] > arr[j + 1]) :
        swap(arr,j,j + 1)
    
    
    return BubbleSort(arr,n,i,j + 1)

def swap(arr,i,j) :
    arr[i],arr[j] = arr[j],arr[i]

    