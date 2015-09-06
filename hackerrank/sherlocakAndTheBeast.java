import java.io.*;
import java.util.*;

// Time complexity: O(1)
public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int T = scanner.nextInt(), i = 0; i < T; ++i) {
            int N = scanner.nextInt();
            int c = 5 * ((2 * N) % 3);
            if (c > N)
                System.out.println(-1);
            else {
                char[] fives = new char[N - c];
                Arrays.fill(fives, '5');
                char[] threes = new char[c];
                Arrays.fill(threes, '3');
                System.out.format("%s%s\n", new String(fives), 
                                            new String(threes));
            }
        }
    }
}
