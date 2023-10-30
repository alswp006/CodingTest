import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int num = 1;
        int[] answer = new int[10];

        for (int i = 0; i < 3; i++) {
            num *= Integer.parseInt(br.readLine());
        }

        while (num!=0){
            answer[num%10] += 1;
            num/=10;
        }

        for (int i : answer){
            bw.write(i+48);
            bw.newLine();
        }
        
        bw.flush();
        bw.close();
    }
}