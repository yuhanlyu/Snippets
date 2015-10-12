import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0, N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; ++i) {
            if (scanner.nextLine().toLowerCase().contains("hackerrank"))
                ++count;
        }
        System.out.println(count);
    }
}
