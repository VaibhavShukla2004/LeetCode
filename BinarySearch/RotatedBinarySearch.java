class Main {
    static int BinarySearch(int [] arr, int target)
    { 
        int lo = 0;
        int hi = arr.length - 1;
        int mid;
        while(lo <= hi)
        {
            mid = (lo + hi)/2;
            if(arr[mid] == target){ return mid; }
            else if(arr[lo] > arr[mid]) //peak is in first area
            {
                if(target < arr[hi]&& target > arr[mid]) 
                {
                    lo = mid + 1;
                }
                else
                {
                    hi = mid - 1;
                }
            }
            else //peak is in second area
            {
                if(target > arr[lo]&&  target < arr[mid]) /*target in sorted area*/
                {
                    hi = mid - 1;
                }
                else 
                {
                    lo = mid + 1;
                }
            }
        }
        
        return -1;
    }
    
    public static void main(String[] args) {
        int [] arr = {5,6,7,8,0,1,2,3,4};
        System.out.println(BinarySearch(arr,3));
    }
}