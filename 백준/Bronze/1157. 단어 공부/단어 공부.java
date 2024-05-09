import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] table = new int[26];
        int max_num = 0;
        int count = 0;
        String s = br.readLine();

        for (char i : s.toCharArray()) table[Character.toUpperCase(i) - 65]++;


        for (int i = 1; i < table.length; i++){
            if (table[max_num] < table[i]) {
                max_num = i;
                count = 0;
            } else if (table[max_num] == table[i]) count += 1;
        }

        if (count >= 1){
            System.out.println("?");
        } else {
            System.out.println((char)(max_num + 65));
        }
    }
}
