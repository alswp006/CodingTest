import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int[][] arr = new int[h + x][w + y];

        for(int i = 0; i < h + x; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < w + y; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (i < h && j < w){
                    if (i >= x && j >= y) arr[i][j] -= arr[i - x][j - y];
                    sb.append(arr[i][j]).append(" ");
                }
            }
            if (i < h) sb.append("\n");
        }

        System.out.println(sb);

    }
}
