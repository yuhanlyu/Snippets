import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        for (int T = scanner.nextInt(), cases = 0; cases < T; ++cases) {
            int R = scanner.nextInt(), C = scanner.nextInt();
            int[][] text = new int[R][C];
            for (int i = 0; i < R; ++i) {
                String s = scanner.next();
                for (int j = 0; j < C; ++j)
                    text[i][j] = s.charAt(j);
            }
            int r = scanner.nextInt(), c = scanner.nextInt();
            int[][] pattern = new int[r][c];
            for (int i = 0; i < r; ++i) {
                String s = scanner.next();
                for (int j = 0; j < c; ++j)
                    pattern[i][j] = s.charAt(j);
            }
            boolean found = false;
            for (int i = 0; i <= R - r && !found; ++i) {
                for (int j = 0; j <= C - c && !found; ++j) {
                    boolean cc = true;
                    for (int k = 0; k < r && !found; ++k) {
                        for (int l = 0; l < c && !found; ++l) {
                            if (text[i+k][j+l] != pattern[k][l]) {
                                cc = false;
                                break;
                            }
                            if (k == r - 1 && l == c - 1)
                                found = true;
                        }
                        if (!cc)
                            break;
                    }
                }
            }
            System.out.println(found ? "YES" : "NO");
        }
    }
}
