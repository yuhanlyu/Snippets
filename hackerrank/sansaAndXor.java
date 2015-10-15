import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int cases = 0; cases < T; ++cases) {
            int N = scanner.nextInt();
            int[] A = new int[N];
            for (int i = 0; i < N; ++i)
                A[i] = scanner.nextInt();
            int result = 0; 
            if (N % 2 == 1)
                for (int i =0; i < N; i += 2)
                    result ^= A[i];
            System.out.println(result);
        }
    }
}
