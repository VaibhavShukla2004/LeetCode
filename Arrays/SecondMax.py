def secondmax(arr) :
    max = arr[0]
    second = arr[0]
    for i in range(len(arr)) :
        if arr[i] > max :
            second = max
            max = arr[i]
    
    return second