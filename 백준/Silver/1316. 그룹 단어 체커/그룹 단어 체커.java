import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int repeat = Integer.parseInt(br.readLine());
        int answer = 0;

        label:
        for (int i = 0; i<repeat; i++){
            List<String> alphabet = new ArrayList<>();
            String[] input = br.readLine().split("");
            List<String> list = new ArrayList<>(Arrays.asList(input));
            alphabet.add(list.get(0));
            for (int j = 1; j<list.size(); j++){
                if (list.get(j).equals(list.get(j-1))){
                    continue;
                }
                if (alphabet.contains(list.get(j))){
                    continue label;
                }
                alphabet.add(list.get(j));
            }
            answer+=1;
        }
        System.out.println(answer);
    }
}