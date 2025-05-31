def unique(arr) :
    i = 0
    for j in range(len(arr)) :
        if(arr[j] != arr[i]) :
            i += 1
            arr[i] = arr[j]
    return arr