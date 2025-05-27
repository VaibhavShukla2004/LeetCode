class Solution: 
    def selectionSort(self, arr):
        for i in range(0, len(arr) - 1):  
            mindx = i
            for j in range(i + 1, len(arr)):  
                if arr[mindx] > arr[j]:
                    mindx = j
                
            if mindx != i:
                arr[i], arr[mindx] = arr[mindx], arr[i]