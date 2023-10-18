import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        int answer=0;

        for (int i : arr){
            if (i-65<17){
                answer+=(i-65)/3+3;
            }else{
                answer+=(i-66)/3+3;
            }
            if (i=='Z'){
                answer-=1;
            }
        }
        System.out.println(answer);
    }
}