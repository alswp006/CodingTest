import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] powers = new int[n];
        String[] names = new String[n];

        st = new StringTokenizer(br.readLine());
        String name = st.nextToken();
        int power = Integer.parseInt(st.nextToken());
        powers[0] = power;
        names[0] = name;

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            name = st.nextToken();
            power = Integer.parseInt(st.nextToken());

            if (powers[i - 1] != power){
                powers[i] = power;
                names[i] = name;
                continue;
            }
            powers[i] = power;
            names[i] = names[i - 1];
        }

        for (int i = 0; i < m; i++) {
            power = Integer.parseInt(br.readLine());
            int num = Arrays.binarySearch(powers, power);
            String answer = num >= 0 ? names[num] : names[num * -1 - 1];
            bw.write(answer + "\n");
        }

        bw.flush();
        bw.close();
    }
}

// bw 사용 :