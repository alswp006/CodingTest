import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] s = br.readLine().toCharArray();
        int temp = 0;
        List<Integer> arr = new ArrayList<>();
        List<Character> cc = new ArrayList<>();
        cc.add('.');
        for(char c : s){
            if (c == '+') {
                arr.add(temp);
                cc.add('+');
                temp = 0;
                continue;
            }
            else if (c == '-') {
                arr.add(temp);
                cc.add('-');
                temp = 0;
                continue;
            }
            temp *= 10;
            temp += ((int) c - '0');
        }
        arr.add(temp);

        int answer = 0;
        boolean iter_flag = true;
        for(int i = 0; i < arr.size(); i++) {
            if (cc.get(i) == '-') iter_flag = false;

            if (iter_flag) answer += arr.get(i);
            else answer -= arr.get(i);
        }

        System.out.println(answer);
    }
}
