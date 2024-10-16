import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long m = Integer.parseInt(st.nextToken());
        long low = 1;
        long high = 0;
        long answer = 0;
        long[] tree = new long[n];

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++){
            long len_tree = Integer.parseInt(st.nextToken());
            if (high < len_tree) high = len_tree;
            tree[i] = len_tree;
        }

        while(low <= high){
            long mid = (high + low) / 2;
            long trees = 0;

            for (long i : tree) {
                if (i > mid) trees += i - mid;
            }

            if (trees >= m){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }

        System.out.println(high);
    }
}
