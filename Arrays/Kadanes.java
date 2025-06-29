import java.util.*;

class Main {
    public static LinkedList<Integer> maxArray(int [] arr)
    {
        if(arr == null||arr.length == 0){ return null; }
        
        int max = Integer.MIN_VALUE;
        int curr = 0;
        
        LinkedList<Integer> maxArray = new LinkedList<>();
        
        for(int i = 0; i < arr.length; i++)
        {
            curr += arr[i];
            if(curr > max)
            {
                max = curr;
                maxArray.offer(arr[i]);
            }
            if(curr < 0)
            {
                curr = 0;
                maxArray.clear();
            }
        }
        
        return maxArray;
    }
    public static void main(String[] args) {
        int [] arr = {-4,-2,-7,8,1};
        System.out.println(maxArray(arr));
    }
}