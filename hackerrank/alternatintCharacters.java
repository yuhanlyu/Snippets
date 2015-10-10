import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int cases = 0; cases < T; ++cases) {
            String string = scanner.next();
            int delete = 0;
            for (int i = 1; i < string.length(); ++i)
                if (string.charAt(i) == string.charAt(i - 1))
                    ++delete;
            System.out.println(delete);
        }
    }
}
