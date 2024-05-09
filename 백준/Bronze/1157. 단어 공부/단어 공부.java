import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] table = new int[26];
        int max_num = 0;
        char answer = 0;
        int count = 0;
        String s = br.readLine();

        for (char i : s.toCharArray()) {
            table[Character.toUpperCase(i) - 65]++;
            max_num = Math.max(max_num, table[Character.toUpperCase(i) - 65]);
        }

        for (int i = 0; i < table.length; i++){
            if (table[i] == max_num){
                max_num = table[i];
                answer = (char)(i + 65);
                count += 1;
            }

            if (count == 2){
                System.out.println("?");
                break;
            }
        }

        if (count == 1){
            System.out.println(answer);
        }
    }
}
