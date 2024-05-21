import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++){
            dp[i] = Integer.MAX_VALUE;
            for (int j = 1; j <= Math.sqrt(i); j++) dp[i] = Math.min(dp[i - j * j] + 1, dp[i]);
        }

        System.out.println(dp[n]);


    }
}
