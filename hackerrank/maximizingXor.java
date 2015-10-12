import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int L = scanner.nextInt(), R = scanner.nextInt(), result = L ^ R;
        result |= result >> 1;
        result |= result >> 2;
        result |= result >> 4;
        System.out.println(result | (result >> 8));
    }
}
