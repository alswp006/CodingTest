import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Set<String> s = new HashSet<>();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        boolean[][] train = new boolean[n][20];

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());

            if (command == 1 || command == 2){
                int train_num = Integer.parseInt(st.nextToken()) - 1;
                int seat = Integer.parseInt(st.nextToken()) - 1;
                train[train_num][seat] = (command == 1);
            } else if (command == 3){
                int train_num = Integer.parseInt(st.nextToken()) - 1;
                train[train_num][19] = false;
                for(int j = 19; j > 0; j--){
                    if (train[train_num][j - 1]){
                        train[train_num][j - 1] = false;
                        train[train_num][j] = true;
                    }
                }
            } else if (command == 4){
                int train_num = Integer.parseInt(st.nextToken()) - 1;
                train[train_num][0] = false;
                for(int j = 0; j < 19; j++){
                    if (train[train_num][j + 1]){
                        train[train_num][j + 1] = false;
                        train[train_num][j] = true;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < 20; j++){
                int temp = 0;
                if (train[i][j]) temp = 1;
                sb.append(temp);
            }
            s.add(sb.toString());
        }

        System.out.println(s.size());
    }
}
