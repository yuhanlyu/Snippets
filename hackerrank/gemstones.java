import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        boolean[] isGem = new boolean[26];
        for (int i = 0; i < isGem.length; ++i)
            isGem[i] = true;
        int result = 26;
        for (int i = 0; i < N; ++i) {
            boolean[] appear = new boolean[26];
            String string = scanner.next();
            for (int j = 0; j < string.length(); ++j)
                appear[string.charAt(j) - 'a'] = true;
            for (int j = 0; j < isGem.length; ++j) {
                if (isGem[j] && !appear[j]) {
                    --result;
                    isGem[j] = false;
                }
            }
        }
        System.out.println(result);
    }
}
