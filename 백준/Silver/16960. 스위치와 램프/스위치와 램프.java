import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int answer = 0;
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        int[] nums = new int[m];
        List<Integer>[] li = new ArrayList[n];

        for (int temp = 0; temp < n; temp++) {
            li[temp] = new ArrayList<>();
            line = br.readLine().split(" ");
            int len_num = Integer.parseInt(line[0]);

            for (int i = 1; i < len_num + 1; i++) {
                int num = Integer.parseInt(line[i]);
                nums[num - 1] += 1;
                li[temp].add(num - 1);
            }
        }


        for (List<Integer> arr : li){
            boolean flag = false;

            for (int j : arr){
                nums[j]--;
                if (nums[j] <= 0){
                    flag = true;
                }
            }

            for (int j : arr){
                nums[j]++;
            }

            if (!flag){
                answer = 1;
                break;
            }
        }

        System.out.println(answer);
    }
}
