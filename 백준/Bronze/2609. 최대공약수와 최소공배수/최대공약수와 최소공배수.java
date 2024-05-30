import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int gcd = 1;

        for (int i = 2; i <= n; i++) {
            if (n % i == 0 && m % i == 0) gcd = i;
        }

        System.out.println(gcd);
        System.out.println(n*m/gcd);
    }
}
