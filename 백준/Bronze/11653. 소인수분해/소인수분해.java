import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int input = Integer.parseInt(br.readLine());
        while(input!=1){
            for (int i = 2; i<=input; i++){
                if (input%i==0){
                    System.out.println(i);
                    input/=i;
                    break;
                }
            }
        }
    }
}