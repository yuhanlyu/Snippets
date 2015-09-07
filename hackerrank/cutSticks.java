import java.io.*;
import java.util.*;

// Time complexity: O(n lg n)
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N + 1];
        for (int i = 0; i < N; ++i)
            A[i + 1] = scanner.nextInt();
        Arrays.sort(A);
        for (int i = 1; i <= N; ++i) {
            if (A[i] != A[i - 1])
                System.out.println(N - i + 1);
        }
    }
}
