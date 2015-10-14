import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        String[] strings = new String[N];
        for (int i = 0; i < N; ++i)
            strings[i] = scanner.nextLine();
        int T = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < T; ++i) {
            String substring = scanner.nextLine();
            Pattern p = Pattern.compile("[\\w\\d_]{1}" + substring + "[\\w\\d_]{1}");
            int count = 0;
            for (int j = 0; j < N; ++j) {
                Matcher m = p.matcher(strings[j]);
                while(m.find()) {
                    ++count;
                }
            }
            System.out.println(count);
        }
    }
}
