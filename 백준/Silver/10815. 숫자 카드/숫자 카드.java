import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[] flag = new boolean[20000001];
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++) flag[Integer.parseInt(st.nextToken()) + 10000000] = true;
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i< m; i++){
            if (flag[Integer.parseInt(st.nextToken()) + 10000000]){
                sb.append(1).append(" ");
                continue;
            }
            sb.append(0).append(" ");
        }
        System.out.println(sb);
    }
}
