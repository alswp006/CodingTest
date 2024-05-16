import java.io.*;

public class Main {
    private static StringBuilder sb = new StringBuilder();

    public static int sumArray(int[][] arr) {
        int sum_num = 0;

        for (int[] i : arr) {
            for (int j : i) sum_num += j;
        }

        return sum_num;
    }

    private static void slice_arr(int n, int[][] arr) {
        int sum_arr = sumArray(arr);
        if (sum_arr == 0) {
            sb.append("0");
            return;
        } else if (sum_arr == n * n) {
            sb.append("1");
            return;
        }

        int[][] temp1 = new int[n / 2][n / 2];
        int[][] temp2 = new int[n / 2][n / 2];
        int[][] temp3 = new int[n / 2][n / 2];
        int[][] temp4 = new int[n / 2][n / 2];

        for (int i = 0; i < n; i++) {
            if (i < n / 2) {
                for (int j = 0; j < n; j++) {
                    if (j < n / 2) {
                        temp1[i][j] = arr[i][j];
                        continue;
                    }
                    temp2[i][j - (n / 2)] = arr[i][j];
                }
                continue;
            }
            for (int j = 0; j < n; j++) {
                if (j < n / 2) {
                    temp3[i - (n / 2)][j] = arr[i][j];
                    continue;
                }

                temp4[i - (n / 2)][j - (n / 2)] = arr[i][j];
            }
        }

        sb.append("(");
        slice_arr(n / 2, temp1);
        slice_arr(n / 2, temp2);
        slice_arr(n / 2, temp3);
        slice_arr(n / 2, temp4);
        sb.append(")");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                arr[i][j] = s.charAt(j) - 48;
            }
        }

        slice_arr(n, arr);

        System.out.println(sb);

    }
}
