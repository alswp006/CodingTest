import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = new int[42];
        int answer = 0;

        for (int i = 0; i<10; i++){
            int num = Integer.parseInt(br.readLine());
            arr[num%42]+=1;
        }
        for (int i : arr){
            if (i>0){
                answer+=1;
            }
        }
        System.out.println(answer);

        bw.flush();
        bw.close();
    }
}