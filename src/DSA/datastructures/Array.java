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



        //Maximum Sum Circular Subarray.
        //for later.....


        //2D array eg.
        int[][] arrayTwoD = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        //arr[row][column]
        System.out.println("2D array 0,0 : " + arrayTwoD[0][0]);
        System.out.println("2D array 2,2 : " + arrayTwoD[2][2]);

        //now useing loop
        for(int i =0; i < arrayTwoD.length; i++){
            for(int j =0; j<arrayTwoD[i].length; j++){
                System.out.println("2D array loop : " + arrayTwoD[i][j]);
            }
        }



        //maxmin 2d array
        printSpiralTraversal();

        //diagonal traversal
        diagonalTraversal();

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
    

    public static void printSpiralTraversal(){
        //print in spiral order
        //we have a 4 by 6 2d matrix and lets  find max row and column and min row and column
        int[][] arr = {
            {4, 2, 8, 1, 5, 7},
            {9, 3, 6, 4, 2, 8},
            {5, 7, 1, 9, 3, 6},
            {8, 4, 2, 7, 6, 1}
        };

        for(int i =0; i<arr.length; i++){
            for(int j =0;j< arr[i].length; j++){
                //System.out.println("Array output : "+ arr[i][j]); 
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();

        }



        int minr = 0;
        int minc = 0;
        int maxr = arr.length - 1;
        int maxc = arr[0].length - 1;
        int te = arr.length * arr[0].length;
        int count = 0;


        System.out.println("Spiral traversal:");

        while (count < te) {

            // Left wall: top to bottom
            for (int i = minr, j = minc; i <= maxr && count < te; i++) {
                System.out.print(arr[i][j] + " ");
                count++;
            }
            minc++;
        
            // Bottom wall: left to right
            for (int i = maxr, j = minc; j <= maxc && count < te; j++) {
                System.out.print(arr[i][j] + " ");
                count++;
            }
            maxr--;
        
            // Right wall: bottom to top
            for (int i = maxr, j = maxc; i >= minr && count < te; i--) {
                System.out.print(arr[i][j] + " ");
                count++;
            }
            maxc--;
        
            // Top wall: right to left
            for (int i = minr, j = maxc; j >= minc && count < te; j--) {
                System.out.print(arr[i][j] + " ");
                count++;
            }
            minr++;
        }

        System.out.println();

    }



    public static void diagonalTraversal(){

        int[][] arr = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        System.out.println("Diagonal traversal:");
        //For a matrix with rows and columns, the number of diagonals is:
        //rows + columns - 1

        int rows = arr.length;
        int col = arr[0].length;
        int totalDiagonals = rows + col - 1;

        for(int diagonal = 0; diagonal < totalDiagonals; diagonal++){
            for(int i =0; i < rows; i++){
                for(int j =0; j < col; j++){
                    if(i+j == diagonal){
                        System.out.print(arr[i][j] + " ");
                    }
                }

            }
        }

        System.out.println();

        //This above solution is good for understanding, but its time complexity is higher because, for every diagonal, it scans the entire matrix.

    }


}
