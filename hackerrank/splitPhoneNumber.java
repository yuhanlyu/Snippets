import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; ++i) {
            String[] s = scanner.nextLine().split("[\\s\\-]");
            System.out.format("CountryCode=%s,LocalAreaCode=%s,Number=%s%n", 
                               s[0], s[1], s[2]);
        }
    }
}
