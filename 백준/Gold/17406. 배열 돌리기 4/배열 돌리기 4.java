import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int[][] original_arr;
    private static int[][] arr;
    private static int[][] rotate_type;
    private static int answer;

    private static void rotate(int x, int y, int s) {
        int start_x = x - s;
        int start_y = y - s;
        int finish_x = x + s;
        int finish_y = y + s;
        int prev_num = 0;

        //상단 가로 라인 오른쪽으로 밀기
        for (int i = start_y; i <= finish_y; i++) {
            int temp = arr[start_x][i];
            arr[start_x][i] = prev_num;
            prev_num = temp;
        }

        //오른쪽 세로 라인 아래로 밀기
        for (int i = start_x + 1; i <= finish_x; i++) {
            int temp = arr[i][finish_y];
            arr[i][finish_y] = prev_num;
            prev_num = temp;
        }

        //하단 가로 라인 왼쪽으로 밀기
        for (int i = finish_y - 1; i >= start_y; i--) {
            int temp = arr[finish_x][i];
            arr[finish_x][i] = prev_num;
            prev_num = temp;
        }

        //왼쪽 세로 라인 위로 밀기
        for (int i = finish_x - 1; i >= start_x; i--) {
            int temp = arr[i][start_y];
            arr[i][start_y] = prev_num;
            prev_num = temp;
        }

        if (s > 1) {
            rotate(x, y, s - 1);
        }

    }

    private static int find_min(int[][] rotate_type) {
        int answer = 1000000000;

        for (int[] i : rotate_type) {
            int temp = 0;
            for (int j : i) {
                temp += j;
            }
            answer = Math.min(answer, temp);
        }

        return answer;
    }

    static void permutation(int[] rotate, int depth, int n) {
        if (depth == n) {
            arr = new int[original_arr.length][original_arr[0].length];

            for (int i = 0; i < original_arr.length; i++){
                for(int j = 0; j < original_arr[i].length; j++) arr[i][j] = original_arr[i][j];
            }

            for(int i = 0; i < n; i++){
                rotate(rotate_type[rotate[i]][0], rotate_type[rotate[i]][1], rotate_type[rotate[i]][2]);
            }
            int temp = find_min(arr);
            answer = Math.min(temp, answer);
            return;
        }


        for (int i = depth; i < n; i++) {
            swap(rotate, depth, i);
            permutation(rotate, depth + 1, n);
            swap(rotate, depth, i);
        }
    }

    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        original_arr = new int[n][m];
        answer = 1000000000;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) original_arr[i][j] = Integer.parseInt(st.nextToken());
        }

        rotate_type = new int[k][3];
        int[] rotate = new int[k];

        for (int i = 0; i < k; i++) rotate[i] = i;
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());

            rotate_type[i][0] = x - 1;
            rotate_type[i][1] = y - 1;
            rotate_type[i][2] = s;
        }

        permutation(rotate, 0, k);
        System.out.println(answer);

    }
}
