import java.io.*;
import java.util.*;
import java.lang.Math;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int M = scanner.nextInt(), N = scanner.nextInt(), R = scanner.nextInt();
        int[][] matrix = new int[M][N];
        for (int i = 0; i < M; ++i)
            for (int j = 0; j < N; ++j)
                matrix[i][j] = scanner.nextInt();
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int level = 0; level < Math.min(M, N) / 2; ++level) {
            int L1 = M - level * 2, L2 = N - level * 2, L = (L1 + L2) * 2 - 4;
            int[] temp = new int[L];
            int[][] indices = new int[L][2];
            int row = level, column = level, current = 0;
            for (int i = 0; i < directions.length; ++i) {
                for (; current < temp.length;) {
                    temp[current] = matrix[row][column];
                    indices[current][0] = row;
                    indices[current++][1] = column;
                    if (row + directions[i][0] < level)
                        break;
                    if (row + directions[i][0] >= M - level)
                        break;
                    if (column + directions[i][1] < level)
                        break;
                    if (column + directions[i][1] >= N - level)
                        break;
                    row += directions[i][0];
                    column += directions[i][1];
                }
                --current;
            }
            int shift = temp.length - R % temp.length;
            for (int i = 0; i < indices.length; ++i)
                matrix[indices[i][0]][indices[i][1]] = temp[(i + shift) % temp.length];
        }
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j)
                System.out.format("%d ", matrix[i][j]);
            System.out.println("");
        }
    }
}
