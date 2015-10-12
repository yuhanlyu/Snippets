import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; ++i) {
            String s = scanner.nextLine();
            System.out.println(s.matches("[a-z]{0,3}[\\d]{2,8}[A-Z]{3,}") ? 
                               "VALID" : "INVALID");
        }
    }
}
