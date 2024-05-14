import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    private static ArrayList<Integer>[] node;
    private static boolean[] visited;
    private static int answer = -1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int computers = Integer.parseInt(br.readLine());
        int v = Integer.parseInt(br.readLine());
        node = new ArrayList[computers + 1];
        for (int i = 0; i < computers + 1; i++) node[i] = new ArrayList<Integer>();

        for (int i = 0; i < v; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());

            node[node1].add(node2);
            node[node2].add(node1);
        }
        visited = new boolean[computers + 1];
        dfs(1);
        System.out.println(answer);
    }

    private static void dfs(int n){
        visited[n] = true;
        answer += 1;

        for (int i : node[n]){
            if (!visited[i]){
                dfs(i);
            }
        }
    }
}
