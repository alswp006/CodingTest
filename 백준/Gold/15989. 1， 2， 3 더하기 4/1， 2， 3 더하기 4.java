import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[10001];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;

        for(int i = 4; i < 10001; i++) dp[i] = 1 + (i / 2) + dp[i - 3];

        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(br.readLine());
            System.out.println(dp[num]);
        }
    }
}
