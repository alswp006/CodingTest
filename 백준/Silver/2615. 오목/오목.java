import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static StringBuilder sb;
    static int[][] arr = new int[19][19];
    static int[][] move = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};

    static void dfs(int x, int y, int user, int depth, int move_type) {
        if (arr[x][y] != user || sb.length() != 0) return;
        if (depth == 4) {
            int nx = x + move[move_type][0];
            int ny = y + move[move_type][1];
            if (nx >= 0 && nx < 19 && ny >= 0 && ny < 19){

                if (arr[nx][ny] != user) {
                    sb.append(user).append("\n");
                    if (move_type == 3){
                        sb.append(x + 1).append(" ").append(y + 1);
                    }else{
                        sb.append(x - (move[move_type][0] * 4) + 1).append(" ").append(y - (move[move_type][1] * 4) + 1);
                    }
                    return;
                }
            } else{
                sb.append(user).append("\n");
                if (move_type == 3){
                    sb.append(x + 1).append(" ").append(y + 1);
                }else{
                    sb.append(x - (move[move_type][0] * 4) + 1).append(" ").append(y - (move[move_type][1] * 4) + 1);
                }
                return;
            }
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + move[i][0];
            int ny = y + move[i][1];

            if (nx < 0 || ny < 0 || nx >= 19 || ny >= 19) continue;

            if (arr[nx][ny] == user) {


                if (depth != 0 && i == move_type) {
                    dfs(nx, ny, user, depth + 1, i);
                    continue;
                }
                if (i != move_type){
                    int nx2 = x - move[i][0];
                    int ny2 = y - move[i][1];

                    if (nx2 >= 0 && ny2 >= 0 && nx2 < 19 && ny2 < 19) {
                        if (arr[nx2][ny2] == user) continue;
                    }
                    dfs(nx, ny, user, 1, i);
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        for (int i = 0; i < 19; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 19; j++) arr[i][j] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < 19; i++) {
            boolean flag = false;
            for (int j = 0; j < 19; j++) {
                if (arr[i][j] > 0) {
                    dfs(i, j, arr[i][j], 0, 5);

                    if (sb.length() != 0) {
                        flag = true;
                        break;
                    }
                }
            }
            if (flag) break;
        }

        if (sb.length() == 0) System.out.println(0);
        else System.out.print(sb);
    }
}

