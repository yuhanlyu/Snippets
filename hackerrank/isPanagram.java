import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            boolean[] map = new boolean[26];
            String line = scanner.nextLine().toLowerCase();
            for (int i = 0; i < line.length(); ++i) {
                if (Character.isLetter(line.charAt(i))) {
                    map[line.charAt(i) - 'a'] = true;
                }
            }
            boolean isPanagram = true;
            for (int i = 0; i < map.length; ++i) {
                if (map[i] == false)
                    isPanagram = false;
            }
            System.out.println(isPanagram ? "pangram" : "not pangram");
        }
    }
}
