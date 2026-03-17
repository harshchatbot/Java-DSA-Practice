package DSA.practise;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class prime_and_reverse {

    public static void main(String[] args){

        //Scanner sc = new Scanner(System.in);  //System.in meaning keyboard input
        List<Integer> intList = new ArrayList<>();
        
        //int n = sc.nextInt();
        int num;
        

        intList.add(2);
        intList.add(6);
        intList.add(7);
        intList.add(9);
        intList.add(11);


        for(int i=0; i <= intList.size() -1; i++){

            num = intList.get(i);
            System.out.println(num);
            int count = 0;

            for(int div = 2; div*div <= num; div++){

                if (num % div == 0) {
                    count++;
                    
                }


            }

            if (count == 0) {

                System.out.println(" : Prime number");
                
            } else {
    
                System.out.println(" : Not a prime number");
    
            }

            

        }

    }
    
}
