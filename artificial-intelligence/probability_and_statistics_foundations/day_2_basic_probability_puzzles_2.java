import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        // In this case wanted condition is : dice are different and             their sum is 6.
        int wantedConditionCount = 0;
        int otherConditionCount = 0;
        
        for (int i=1; i<=6; i++){
            for (int j=1; j<=6; j++){
                if (i != j && i + j == 6) {
                    wantedConditionCount++;
                } else{
                    otherConditionCount++;
                }
            }
        }
        
        System.out.println(wantedConditionCount);
        System.out.println(otherConditionCount);
        //Answer in plain text:
        // 4 / (4+32) = 4/36 = 1/9
    }
}