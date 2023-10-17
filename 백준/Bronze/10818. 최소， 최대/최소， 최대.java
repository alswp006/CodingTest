import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int min_value = 1000001;
        int max_value = -1000001;

        for (int i = 0; i<n; i++){
            int num = Integer.parseInt(st.nextToken());
            if (num<min_value){
                min_value=num;
            }
            if (num>max_value){
                max_value=num;
            }
        }
        bw.write(min_value + " ");
        bw.write(max_value + " ");

        bw.flush();
        bw.close();
    }
}