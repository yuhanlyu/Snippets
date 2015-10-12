import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        String[] s = new String[N];
        for (int i = 0; i < N; ++i)
            s[i] = scanner.nextLine();
        int T = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < T; ++i) {
            String word = scanner.nextLine();
            int count = 0;
            for (int j = 0; j < N; ++j) {
                Pattern pattern = Pattern.compile(word.substring(0, word.length() - 2) + "(z|s)e");
                Matcher matcher = pattern.matcher(s[j]);
                while (matcher.find())
                    count++;
            }
            System.out.println(count);
        }
    }
}
