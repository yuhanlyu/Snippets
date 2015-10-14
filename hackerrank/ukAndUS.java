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
            String pattern = scanner.nextLine();
            String pattern2 = pattern.replaceAll("our", "or");
            int count = 0;
            for (int j = 0; j < N; ++j) {
                String[] text = strings[j].split(" ");
                for (int k = 0; k < text.length; ++k)
                    if (text[k].equals(pattern) || text[k].equals(pattern2))
                        ++count;
            }
            System.out.println(count);
        }
    }
}
