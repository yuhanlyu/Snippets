import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        String input = new Scanner(System.in).next();
        int[] histogram = new int[26];
        for (int i = 0; i < input.length(); ++i)
            ++histogram[input.charAt(i) - 'a'];
        int odd = 0;
        for (int i = 0; i < histogram.length; ++i)
            if (histogram[i] % 2 == 1)
                ++odd;
        System.out.println(odd <= 1 ? "YES" : "NO");
    }
}
