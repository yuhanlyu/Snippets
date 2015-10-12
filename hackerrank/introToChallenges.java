import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int V = scanner.nextInt(), n = scanner.nextInt(), i = 0; 
                                                               i < n; ++i)
            if (scanner.nextInt() == V)
                System.out.println(i);
    }
}
