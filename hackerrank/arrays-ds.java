import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; ++i)
            A[i] = scanner.nextInt();
        for (int i = N - 1; i >= 0; --i)
            System.out.format("%d ", A[i]);
    }
}
