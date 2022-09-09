import java.lang.*;
import java.util.*;

public class Main {
    public static void processArray(ArrayList<Integer> arr) {
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i) / 100 == 0 && arr.get(i + 1) / 100 == 0) {
                if(arr.get(i)<arr.get(i+1)){
                    arr.remove(i+1);
                }
                else{
                    arr.remove(i);
                }
                i--;
            }
        }

        for (Integer i : arr) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        while (true) {
            int i = sc.nextInt();
            if (i >= 0)
                arr.add(i);
            else
                break;
        }
        processArray(arr);
    }
}