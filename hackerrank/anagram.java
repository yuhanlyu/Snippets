import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int cases = 0; cases < T; ++cases) {
            String s = scanner.next();
            if (s.length() % 2 == 1) {
                System.out.println("-1");
                continue;
            }
            String s1 = s.substring(0, s.length() / 2);
            String s2 = s.substring(s.length() / 2, s.length());
            int[] c1 = new int[26], c2 = new int[26];
            for (int i = 0; i < s1.length(); ++i)
                ++c1[s1.charAt(i) - 'a'];
            for (int i = 0; i < s2.length(); ++i)
                ++c2[s2.charAt(i) - 'a'];
            int result = 0;
            for (int i = 0; i < c1.length; ++i)
                result += Math.max(c1[i], c2[i]) - Math.min(c1[i], c2[i]);
            System.out.println(result / 2);
        }
    }
}
