public class bigo_on {

   
        //O(n)
        public static void printItems(int n) {
            for(int i=0;i<n;i++){
                System.out.println(i);
            }
        }

        //O(n square)
        public static void printItems2(int n) {
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    System.out.println(i + " "+ j);
                }
            }

            

        }

        //O(n square)
        public static void printItems3(int n) {
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    System.out.println(i + " "+ j);
                }
            }

            for(int k=0;k<n;k++){
                System.out.println(k);
            }

            

        }
    
    
    
        // DO NOT CHANGE THE MAIN METHOD BELOW
        public static void main(String[] args) {
            printItems(10);
            printItems2(10);
            printItems3(10);
        }

    
}
