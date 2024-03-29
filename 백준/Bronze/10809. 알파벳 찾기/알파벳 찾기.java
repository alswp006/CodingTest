import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] str = br.readLine().toCharArray();
        int[] answer_arr = new int[26];
        StringBuilder answer = new StringBuilder();
        Arrays.fill(answer_arr,-1);

        for (int i = 0; i<str.length; i++){
            int ascii_alphabet = (int)str[i]-97;
            if (answer_arr[ascii_alphabet]==-1){
                answer_arr[ascii_alphabet] = i;
            }
        }

        for (int i : answer_arr){
            answer.append(i);
            answer.append(" ");
        }
        System.out.println(answer);
    }
}