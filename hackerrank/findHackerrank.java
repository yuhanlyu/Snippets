import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; ++i) {
            String s = scanner.nextLine();
            boolean start = s.startsWith("hackerrank"), 
                      end = s.endsWith("hackerrank");
            if (start && end)
                System.out.println("0");
            else if (end)
                System.out.println("2");
            else if (start)
                System.out.println("1");
            else
                System.out.println("-1");
        }
    }
}
