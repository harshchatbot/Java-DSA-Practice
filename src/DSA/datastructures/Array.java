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
    }

}
