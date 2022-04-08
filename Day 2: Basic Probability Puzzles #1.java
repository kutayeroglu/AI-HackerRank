import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int targetSum = 9;
        int aboveSumCount = 0;
        int underSumCount = 0;
        
        for(int i = 1; i <= 6; i++){
            for (int j = 1; j <= 6; j++){
                 if (i+j <= 9){
                   underSumCount++;  
                 } else {
                     aboveSumCount++;
                 }
            }
        }
        
        System.out.println(underSumCount); //30
        System.out.println(aboveSumCount); //6
        // Answer in plain text: 30/(30+6) = 5/6
    }
}