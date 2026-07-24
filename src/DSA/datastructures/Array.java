package DSA.datastructures;

import java.util.Arrays;

public class Array {
    public static void main (String[] args){

        Integer arr[] = new Integer[5];
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 3;
        arr[4] = 4;

        System.out.println("Array Test : " + arr[2]);

        
        Integer arr2[] = {1,2,3,4,5,6};

        for(int i = 0; i<arr2.length;i++){
            System.out.println("Array loop : " + arr2[i]);
        }


        //lets swap
        int arrSwap[] = new int[]{1,2,3,4,5};
        swap(arrSwap, 0,1 );
        System.out.println("swapped array : " +  Arrays.toString(arrSwap));



        //secondLargest
        int arr4[] = {22,12,44,8,66,66}; 
        secondLargest(arr4);
        
    }

    //swap function
    static void swap(int[] arr3 , int i , int j){
        int temp = arr3[i];
        arr3[i] = arr3[j];
        arr3[j] = temp;

    }

    //find 2nd largest num. in array
    static void secondLargest(int[] arr4){
        Arrays.sort(arr4); // sort array in ascending order
        //if repeated numb edge case handle
        int largest = arr4[arr4.length - 1];
        System.out.println("largest number in array : " + largest);

        for(int i = arr4.length -2; i >= 0; i--){
            if(arr4[i] < largest){
                
                System.out.println("Second largest number in array : " + arr4[i]);
                break;

            }

        }
        System.out.println("Second largest array : " + Arrays.toString(arr4));

        //DNF algo
        int[] colors = {1, 1, 2, 2, 0, 1, 2, 2, 1};
        sortColors(colors);
        System.out.println("DNF algo : "+ Arrays.toString(colors));



        //Majority Element
        int[] majorityArr = {3, 3, 0, 3, 1, 3, 2}; // with majority element
        //int[] majorityArr = {3, 3, 0, 1, 1, 3, 2}; //without majority element
        majorityElement(majorityArr);



        //Maximum Subarray
        int[] subArr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Maximum Subarray : " + maxSubArray(subArr));

    }



    //Sort Colors problem, commonly solved in-place using Dijkstra’s Dutch National Flag approach.
    static void sortColors(int[] nums){

        int low = 0;
        int mid = 0;
        int high = nums.length -1;

        while( mid <= high){

            if(nums[mid] == 0){
                swap(nums, mid, low);
                low++;
                mid++;
            }
            else if(nums[mid] == 1){
                mid++;
            }
            else {
                swap(nums, mid, high);
                high--;
            }

        }

    }


    //Majority element : Given an array, find the element that appears more than n / 2 times.
    static void majorityElement(int[] majorityArr) {
        //here n = 7
        //Arrays.sort(majorityArr); //if using boyer-moore voting algo then this sort is not required
        System.out.println("Sorted Majority Array : " + Arrays.toString(majorityArr));

        //find middle element
        int middleIndex = majorityArr.length / 2;
        System.out.println("Middle num : "+ majorityArr[middleIndex]);

        //but the best approach to do this is by using : Boyer–Moore Voting Algorithm
        //Boyer–Moore works by cancelling one majority candidate against one different element.

        //we need two variables
        int candidate = 0;
        int count = 0;
        int candidateCount = 0;

        for(int i = 0; i< majorityArr.length; i++){
            if(count == 0){
                candidate = majorityArr[i];
                
            } 

            if(majorityArr[i] == candidate){
                count++;
            } else {
                count--;

            }

    }

    System.out.println("Majority Element : " + candidate);

        for(int i =0; i<majorityArr.length; i++){
            if(majorityArr[i] == candidate){
                candidateCount++;
            }
        }

        if(candidateCount > majorityArr.length / 2){
            System.out.println("We do have a majority element");
        }else {
            System.out.println("There is no majority element");
        }    

    }



    public static int maxSubArray(int[] subArr){

        //Kadane’s algorithm
        var currentSum = subArr[0]; //Why initialize using nums[0] instead of 0? .Because this also handles arrays containing only negative numbers,
        var maximumSum = subArr[0];

        for(int i =1;i<subArr.length; i++){
            //Math.max(a, b)
            currentSum = Math.max(subArr[i], currentSum + subArr[i]);
            maximumSum = Math.max(maximumSum , currentSum);

        }

        return maximumSum;
    }
    


}
