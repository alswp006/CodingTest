import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] S = new int[20];

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            String operator = st.nextToken();
            if (operator.equals("all")) {
                for (int j = 0; j < 20; j++) S[j] = 1;
                continue;
            } else if (operator.equals("empty")){
                for (int j = 0; j < 20; j++) S[j] = 0;
                continue;
            }

            int x = Integer.parseInt(st.nextToken());

            if (operator.equals("add")){
                S[x-1] = 1;
            } else if (operator.equals("remove")){
                S[x-1] = 0;
            } else if (operator.equals("check")){
                if (S[x-1] == 1){
                    bw.write("1\n");
                } else{
                    bw.write("0\n");
                }
            } else if (operator.equals("toggle")){
                S[x-1] = Math.abs(S[x-1] - 1);
            }
        }
        bw.flush();
        bw.close();
    }
}
