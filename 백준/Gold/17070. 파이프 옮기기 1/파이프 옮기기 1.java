import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static int n;
    private static int answer = 0;
    private static int[][] arr;

    private static void dfs(int x, int y, int type) {
        if (x < 0 || y < 0 || x >= n || y >= n || arr[x][y] == 1) {
            return;
        }
        if (x == n - 1 && y == n - 1) {
            answer++;
            return;
        }

        if (type != 0){
            dfs(x + 1, y, 2);
        }
        if (type != 2){
            dfs(x, y + 1, 0);
        }
        if (x + 1 < n && y + 1 < n && arr[x+1][y] == 0 && arr[x][y+1] == 0){
            dfs(x + 1, y + 1, 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) arr[i][j] = Integer.parseInt(st.nextToken());
        }

        //type : 0 = 가로, 1 = 대각선, 2 = 세로
        dfs(0, 1, 0);
        System.out.println(answer);
    }
}