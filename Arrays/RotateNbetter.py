def rotateLeft(arr, r=0):
    r = r % len(arr)
    return arr[r:] + arr[:r]
