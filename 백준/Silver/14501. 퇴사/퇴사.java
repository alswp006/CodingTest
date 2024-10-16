import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            if (i + t < n + 1) {
                dp[i + t] = Math.max(dp[i + t], dp[i] + p);
            }
            if (i != 0 && dp[i] > dp[i+1]){
                dp[i + 1] = dp[i];
            }

        }

        System.out.println(dp[n]);
    }
}
