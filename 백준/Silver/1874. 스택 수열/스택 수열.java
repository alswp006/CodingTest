import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> arr = new Stack<>();
        int flag = 1;
        int num = Integer.parseInt(br.readLine());

        for (int i = 1; i < n + 1; i++){
            arr.push(i);
            sb.append("+\n");

            while (!arr.isEmpty()){
                int temp = arr.pop();
                if (flag == n){
                    break;
                }
                if (temp == num){
                    num = Integer.parseInt(br.readLine());
                    sb.append("-\n");
                    flag+=1;
                }else{
                    arr.push(temp);
                    break;
                }
            }
        }
        for(int i = flag; i < n; i++) br.readLine();
        if (arr.isEmpty()){
            System.out.println(sb.append("-"));
        }else{
            System.out.println("NO");
        }

    }
}
