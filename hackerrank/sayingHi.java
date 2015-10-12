import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; ++i) {
            String s = scanner.nextLine();
            if (s.toLowerCase().matches("^hi (?!d).*"))
                System.out.println(s);
        }
    }
}
