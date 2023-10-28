import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int[][] array1 = new int[x][y];

        for(int arr = 0; arr<2; arr++){
            for (int i = 0; i<x; i++){
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j<y; j++){
                    array1[i][j] += Integer.parseInt(st.nextToken());
                }
            }
        }
        for (int[] y_arr : array1){
            for (int num : y_arr){
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}