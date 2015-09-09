import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt(), M = scanner.nextInt();
        String[] mins = {"zero", "one minute", "two minutes", "three minutes", "four minutes", 
            "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes",
            "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes", 
            "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes", 
            "eighteen minutes", "nineteen minutes", "twenty minutes", "twenty one minutes",
            "twenty two minutes", "twenty three minutes", "twenty four minutes", 
            "twenty five minutes", "twenty six minutes", "twenty seven minutes", 
            "twenty eight minutes", "twenty nine minutes", "half"};
        String[] hours = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "one"};
        if (M == 0)
            System.out.println(hours[H] + " o\' clock");
        else if (M <= 30)
            System.out.println(mins[M] + " past " + hours[H]);
        else
            System.out.println(mins[60 - M] + " to " + hours[H + 1]);
    }
}
