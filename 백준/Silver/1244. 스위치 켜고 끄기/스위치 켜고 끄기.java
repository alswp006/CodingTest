import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) arr[i] = (Integer.parseInt(st.nextToken()));
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int light = Integer.parseInt(st.nextToken());
            if (gender == 1) {
                for (int j = light - 1; j < n; j += light) {
                    arr[j] = Math.abs(arr[j] - 1);
                }
            } else {
                arr[light - 1] = Math.abs(arr[light - 1] - 1);
                int temp = 1;
                while (light - 1 - temp >= 0 && light - 1 + temp < n) {
                    if (arr[light - 1 - temp] == arr[light - 1 + temp]) {
                        arr[light - 1 - temp] = Math.abs(arr[light - 1 - temp] - 1);
                        arr[light - 1 + temp] = Math.abs(arr[light - 1 + temp] - 1);
                    } else {
                        break;
                    }

                    temp += 1;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i / 20 != 0 && i % 20 == 0) {
                sb.append("\n");
            }
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb);
    }
}
