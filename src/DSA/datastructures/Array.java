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

        //lets find out the second largest number in the array

        //lets swap
        int arrSwap[] = new int[]{1,2,3,4,5};
        swap(arrSwap, 0,1 );
        System.out.println("swapped array : " +  Arrays.toString(arrSwap));

        
    }

    static void swap(int[] arr3 , int i , int j){
        int temp = arr3[i];
        arr3[i] = arr3[j];
        arr3[j] = temp;

    }
}
