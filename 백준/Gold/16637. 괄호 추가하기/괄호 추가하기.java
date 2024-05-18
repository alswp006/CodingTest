import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int answer;
    static int[] num;
    static char[] oper;

    static int calculate(int x, int y, char operator){
        switch (operator){
            case '+' : return x+y;
            case '-' : return x-y;
            case '*' : return x*y;
            default : return 0;
        }
    }
    static void find_answer(int idx, int result){
        if (idx >= num.length){
            answer = Math.max(answer, result);
            return;
        }
        find_answer(idx + 1, calculate(result, num[idx], oper[idx - 1]));

        if (idx + 1 < num.length) find_answer(idx + 2, calculate(result, calculate(num[idx], num[idx + 1], oper[idx]), oper[idx - 1]));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[] str = br.readLine().toCharArray();
        answer = -1000000001;
        if (n == 1){
            System.out.println(str[0]);
            return;
        }
        n = str.length;
        num = new int[n / 2 + 1];
        oper = new char[n / 2];

        for (int i = 0; i < n; i++){
            if (i%2==0) num[i/2] = str[i] - '0';
            else oper[i/2] = str[i];
        }

        find_answer(1, num[0]);
        System.out.println(answer);
    }
}
