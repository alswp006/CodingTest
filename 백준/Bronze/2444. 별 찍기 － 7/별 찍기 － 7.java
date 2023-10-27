import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int num = Integer.parseInt(br.readLine());
        sb.append("*");
        for (int i = num-1; i>=0; i--){
            for (int j = 0; j<i; j++){
                bw.write(" ");
            }
            bw.write(String.valueOf(sb));
            bw.newLine();
            sb.append("**");
        }
        sb.delete(0,2);
        for (int i = 1; i<num; i++){
            sb.delete(0,2);
            for (int j = 0; j<i; j++){
                bw.write(" ");
            }
            bw.write(String.valueOf(sb));
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}