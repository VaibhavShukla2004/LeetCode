def rotateLeft(arr,r = 0) :
    r = r%len(arr)
    
    rotated = []
    for i in range(r,len(arr)) :
        rotated.append(arr[i])
    
    for i in range(r) : 
        rotated.append(arr[i])
    
    return rotated

def rotateRight(arr,r=0):
    r = r%(len(arr))
    rotated = []
    for i in range(len(arr) - r,len(arr)) :
        rotated.append(arr[i])
        
    for i in range(len(arr) - r):
        rotated.append(arr[i])
    
    return rotated 