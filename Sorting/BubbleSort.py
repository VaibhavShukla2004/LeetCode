class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
       for i in range(0,len(arr) - 1) :
           for j in range(0,len(arr) - i - 1) :
               if arr[j] > arr[j + 1] :
                   temp = arr[j]
                   arr[j] = arr[j + 1]
                   arr[j + 1] = temp
                
                
                