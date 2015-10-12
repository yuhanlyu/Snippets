import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; ++i) {
            long x = scanner.nextLong();
            System.out.println(~x & 0xFFFFFFFFL);
        }
    }
}
