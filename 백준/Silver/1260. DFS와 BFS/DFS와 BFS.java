import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int n;
    private static ArrayList<Integer>[] li;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        visited = new boolean[n + 1];
        li = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            li[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int node = Integer.parseInt(st.nextToken());
            int fin_node = Integer.parseInt(st.nextToken());
            li[node].add(fin_node);
            li[fin_node].add(node); // 양방향 그래프인 경우 추가
        }

        for (int i = 0; i <= n; i++){
            Collections.sort(li[i]);
        }

        dfs(v);
        visited = new boolean[n + 1];
        System.out.println();
        bfs(v);
    }

    private static void dfs(int v){
        visited[v] = true;
        System.out.print(v + " ");

        for (int i = 0; i < li[v].size(); i++){
            int nextNode = li[v].get(i);
            if (!visited[nextNode]){
                dfs(nextNode);
            }
        }
    }

    private static void bfs(int v){
        Queue<Integer> q = new LinkedList<>();
        visited[v] = true;
        q.add(v);

        while (!q.isEmpty()){
            int node = q.remove();
            System.out.print(node + " ");

            for (int i = 0; i < li[node].size(); i++){
                int nextNode = li[node].get(i);
                if (!visited[nextNode]){
                    visited[nextNode] = true;
                    q.add(nextNode);
                }
            }
        }
    }
}