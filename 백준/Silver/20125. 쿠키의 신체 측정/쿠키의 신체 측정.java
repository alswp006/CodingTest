import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int line = -1;
        int[] body = new int[5];
        int[] heart = new int[2];

        // 심장 위치 찾기
        while (heart[1] == 0) {
            line += 1;
            String st = br.readLine();
            for (int i = 0; i < n; i++) {
                if (st.charAt(i) == '*') {
                    heart[0] = line + 1;
                    heart[1] = i;
                    break;
                }
            }
        }

        // 팔 길이 구하기
        int start = -1;
        int last = n - 1;
        String st = br.readLine();
        for (int i = 0; i < n; i++) {
            if (st.charAt(i) == '*' && start == -1) start = i;
            if (st.charAt(i) == '_' && start != -1) {
                last = i - 1;
                break;
            }
        }
        body[0] = heart[1] - start;
        body[1] = last - heart[1];
        line += 1;

        //몸 길이 구하기
        boolean flag = true;
        while (flag) {
            line += 1;
            st = br.readLine();
            for (int i = 0; i < n; i++) {
                if (st.charAt(i) == '*' && i == heart[1] - 1) {
                    flag = false;
                    break;
                }
            }
        }
        body[2] = line - 1 - heart[0];

        //다리 길이 구하기
        body[3] = 1;
        body[4] = 1;
        while (line + 1 < n) {
            st = br.readLine();
            for (int i = 0; i < n; i++) {
                if (st.charAt(i) == '*' && i == heart[1] - 1) body[3] += 1;
                if (st.charAt(i) == '*' && i == heart[1] + 1) body[4] += 1;
            }
            line += 1;
        }

        sb.append(heart[0] + 1).append(" ").append(heart[1] + 1).append("\n");
        for (int i : body) {
            sb.append(i).append(" ");
        }

        System.out.println(sb);
    }
}
