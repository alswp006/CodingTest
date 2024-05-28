import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true){
            String end_point = br.readLine();
            if (end_point.equals("end")) break;
            boolean flag = true;
            int vowel_cnt = 0;
            int consonant_cnt = 0;
            char pre_word = ' ';
            for(int i = 0; i < end_point.length(); i++){
                char c = end_point.charAt(i);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    flag = false;
                    vowel_cnt += 1;
                    consonant_cnt = 0;
                } else{
                    vowel_cnt = 0;
                    consonant_cnt += 1;
                }

                if (consonant_cnt == 3 || vowel_cnt == 3){
                    flag = true;
                    break;
                }

                if (pre_word == c){
                    if (pre_word != 'e' && pre_word != 'o') {
                        flag = true;
                        break;
                    }

                }
                pre_word = end_point.charAt(i);
            }

            if (!flag) sb.append("<").append(end_point).append("> is acceptable.\n");
            else sb.append("<").append(end_point).append("> is not acceptable.\n");
        }

        System.out.println(sb);
    }
}
