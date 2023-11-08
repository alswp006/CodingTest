import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> output = new ArrayList<>();
        int input = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < input; i++){
            String[] s = br.readLine().split(" ");
            if(s[0].length() != s[1].length()){
                output.add(String.format("%s & %s are NOT anagrams.", s[0], s[1]));
                continue;
            }

            String x = s[0].chars()        // IntStream
                    .sorted()
                    .collect(StringBuilder::new,
                            StringBuilder::appendCodePoint,
                            StringBuilder::append)
                    .toString();

            String y = s[1].chars()        // IntStream
                    .sorted()
                    .collect(StringBuilder::new,
                            StringBuilder::appendCodePoint,
                            StringBuilder::append)
                    .toString();

            if (x.equals(y)){
                output.add(String.format("%s & %s are anagrams.", s[0], s[1]));
            }else{
                output.add(String.format("%s & %s are NOT anagrams.", s[0], s[1]));
            }
        }
        for (String s : output){
            System.out.println(s);
        }
    }
}