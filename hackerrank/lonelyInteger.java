import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int result = 0, N = scanner.nextInt();
        for (int i = 0; i < N; ++i)
            result ^= scanner.nextInt();
        System.out.println(result);
    }
}
