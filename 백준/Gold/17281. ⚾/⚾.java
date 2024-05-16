import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int answer;
    private static int[][] inning;
    static int[] base;

    private static int play(int[] player_seq) {
        int score = 0;
        int pres_player = 0;
        int out_count = 0;

        for (int[] ints : inning) {
            base = new int[4];
            while (out_count < 3) {
                if (ints[player_seq[pres_player]] == 0) {
                    out_count++;
                } else {
                    score += go_base(ints[player_seq[pres_player]]);
                }
                pres_player++;
                if (pres_player == 9){
                    pres_player = 0;
                }
            }
            out_count = 0;
        }
        return score;
    }


    static int go_base(int n) {
        int temp = 0;

        if (n == 4){
            temp++;
        }

        for (int i = 3; i > 0; i--) {
            if (base[i] == 1) {
                base[i] = 0;
                if (i + n > 3) {
                    temp++;
                    continue;
                }
                base[i + n] = 1;
            }
        }
        if (n != 4){
            base[n] = 1;
        }

        return temp;
    }

    static void permutation(int[] arr, int depth, int n) {
        if (depth == n) {
            answer = Math.max(answer, play(arr));
            return;
        }

        if (depth == 3) {
            permutation(arr, depth + 1, n);
            return;
        }

        for (int i = depth; i < n; i++) {
            if (i == 3){
                continue;
            }
            swap(arr, depth, i);
            permutation(arr, depth + 1, n);
            swap(arr, depth, i);
        }
    }

    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        inning = new int[n][9];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) inning[i][j] = Integer.parseInt(st.nextToken());
        }

        int[] player_seq = {3, 1, 2, 0, 4, 5, 6, 7, 8};
        permutation(player_seq, 0, 9);
        System.out.println(answer);
    }

}
