import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; ++i) {
            String s = scanner.nextLine();
            boolean match = s.matches("\\d{5} ((C)|(CPP)|(JAVA)|(PYTHON)|(PERL)|(PHP)|(RUBY)|(CSHARP)|(HASKELL)|(CLOJURE)|(BASH)|(SCALA)|(ERLANG)|(CLISP)|(LUA)|(BRAINFUCK)|(JAVASCRIPT)|(GO)|(D)|(OCAML)|(R)|(PASCAL)|(SBCL)|(DART)|(GROOVY)|(OBJECTIVEC))");
            System.out.println(match ? "VALID" : "INVALID");
        } 
    }
}
