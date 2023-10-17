import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        String[] arr = br.readLine().split(" ");
        int n =Integer.parseInt(arr[0]);
        int[] basket = new int[n];

        for (int i = 0; i<n; i++){
            basket[i] = i+1;
        }
        for (int i = 0; i<Integer.parseInt(arr[1]); i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;

            int temp = basket[x];
            basket[x] = basket[y];
            basket[y] = temp;
        }

        for (int i : basket){
            bw.write(i + " ");
        }
        bw.flush();
        bw.close();
    }
}