import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        List<Integer> arr = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++){
            int x = Integer.parseInt(br.readLine());
            arr.add(x);
        }
        Collections.sort(arr);

        for (int i : arr){
            sb.append(i).append("\n");
        }

        System.out.println(sb);
    }
}
