import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int n;
    private static ArrayList<Integer>[] li;
    private static boolean[] visited;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        li = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            li[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int node = Integer.parseInt(st.nextToken());
            int fin_node = Integer.parseInt(st.nextToken());
            li[node].add(fin_node   );
            li[fin_node].add(node);
        }

        for (int i = 0; i <= n; i++){
            Collections.sort(li[i]);
        }

        visited = new boolean[n + 1];
        dfs(v);
        sb.append("\n");
        visited = new boolean[n + 1];
        bfs(v);

        System.out.println(sb);
    }

    private static void dfs(int v){
        visited[v] = true;
        sb.append(v).append(" ");

        for (int nextNode : li[v]){
            if (!visited[nextNode]){
                dfs(nextNode);
            }
        }
    }

    private static void bfs(int v){
        visited[v] = true;
        Queue<Integer> q = new LinkedList<>();
        q.add(v);

        while (!q.isEmpty()){
            int node = q.remove();
            sb.append(node).append(" ");

            for (int nextNode : li[node]){
                if (!visited[nextNode]){
                    visited[nextNode] = true;
                    q.add(nextNode);
                }
            }
        }
    }
}