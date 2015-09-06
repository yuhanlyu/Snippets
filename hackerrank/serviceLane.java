import java.io.*;
import java.util.*;

// Time complexity: O(T + N)
// Space complexity: O(N)
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(), T = scanner.nextInt();
        int[] one = new int[N + 1], two = new int[N + 1], three = new int[N + 1];
        for (int i = 1; i <= N; ++i) {
            one[i] = one[i - 1];
            two[i] = two[i - 1];
            three[i] = three[i - 1];
            switch(scanner.nextInt()) {
                case 1:
                    ++one[i];
                    break;
                case 2:
                    ++two[i];
                    break;
                case 3:
                    ++three[i];
            }
        }
        for (int cases = 0; cases < T; ++cases) {
            int i = scanner.nextInt(), j = scanner.nextInt();
            if (one[i] != one[j + 1])
                System.out.println(1);
            else if (two[i] != two[j + 1])
                System.out.println(2);
            else
                System.out.println(3);
        }
    }
}
