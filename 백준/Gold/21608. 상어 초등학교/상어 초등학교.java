import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[][] move_type = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    static int[][] satisfy;
    static int[][] arr;

    static boolean check_std(int me, int friend) {
        for (int i : satisfy[me]) {
            if (i == friend) return true;
        }
        return false;
    }

    static int check_satis(int x, int y, int std_num) {
        int temp = 0;

        for (int i = 0; i < 4; i++) {
            int nx = x + move_type[i][0];
            int ny = y + move_type[i][1];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
            if (arr[nx][ny] != -1 && check_std(std_num, arr[nx][ny])) temp++;
        }

        return temp;
    }

    static int check_empty(int x, int y) {
        int temp = 0;
        for (int k = 0; k < 4; k++) {
            int nx = x + move_type[k][0];
            int ny = y + move_type[k][1];

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
            if (arr[nx][ny] == -1) temp++;
        }
        return temp;
    }

    static int[] check_max_empty() {
        int[] place = {0, 0, 0};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] != -1) continue;

                int temp = check_empty(i, j);

                if (place[2] < temp) {
                    place[0] = i;
                    place[1] = j;
                    place[2] = temp;
                }
            }
        }

        if (place[2] == 0 && arr[place[0]][place[1]] != -1) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (arr[i][j] == -1) {
                        place[0] = i;
                        place[1] = j;
                        return place;
                    }
                }
            }
        }
        return place;
    }

    static void insert_std(int std_num) {
        int pres_satis = 0;
        int[] place = {0, 0, 0};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i][j] != -1) {
                    continue;
                }
                int temp = check_satis(i, j, std_num);
                if (temp > pres_satis) {
                    pres_satis = temp;
                    place[0] = i;
                    place[1] = j;
                    place[2] = check_empty(i, j);
                } else if (temp == pres_satis) {
                    int empty = check_empty(i, j);
                    if (empty > place[2]) {
                        place[0] = i;
                        place[1] = j;
                        place[2] = empty;
                    }
                }
            }
        }

        if (pres_satis == 0) {
            place = check_max_empty();
        }

        arr[place[0]][place[1]] = std_num;
//        각 학생이 배치될때마다 테이블 확인
//        for(int[] i : arr){
//            for (int j:i){
//                System.out.print(j);
//            }
//            System.out.println();
//        }
//        System.out.println();
    }

    static int cal_satis() {
        int temp = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp += (int) Math.pow(10, check_satis(i, j, arr[i][j])-1);
            }
        }

        return temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] std_seq = new int[n * n];
        arr = new int[n][n];
        satisfy = new int[n * n][4];

        for (int i = 0; i<n; i++){
            for(int j = 0; j < n; j++) arr[i][j] = -1;
        }
        for (int i = 0; i < n * n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int std = Integer.parseInt(st.nextToken()) - 1;
            std_seq[i] = std;
            for (int j = 0; j < 4; j++) satisfy[std][j] = Integer.parseInt(st.nextToken()) - 1;
        }
        arr[1][1] = std_seq[0];

        for (int i = 1; i < n * n; i++) insert_std(std_seq[i]);

        System.out.println(cal_satis());
    }
}
