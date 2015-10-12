import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int N = scanner.nextInt(), i = 0; i < N; ++i) {
            String s = scanner.next();
            System.out.println(s.matches("[A-Z]{5}\\d{4}[A-Z]") ? "YES" : "NO");
        }
    }
}
