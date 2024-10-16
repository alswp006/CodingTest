import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    static BufferedWriter bw;
    static List<Integer>[] li;
    static boolean[] visited;
    static StringBuilder sb;

    public static void dfs(int v){
        if (visited[v]) return;

        visited[v] = true;
        sb.append(v).append(" ");
        for (int i : li[v]){
            dfs(i);
        }
    }

    public static void bfs(int v){
        Deque<Integer> q = new ArrayDeque<>();
        q.add(v);

        while (!q.isEmpty()){
            int node = q.removeFirst();
            if (visited[node]) continue;
            sb.append(node).append(" ");
            visited[node] = true;

            for (int i : li[node]){
                if (!visited[i]){
                    q.add(i);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        li = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < n + 1; i++){
            li[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            li[x].add(y);
            li[y].add(x);
        }
        for (int i = 0; i < n + 1; i++){
            Collections.sort(li[i]);
        }

        dfs(v);
        sb.append("\n");
        visited = new boolean[n + 1];

        bfs(v);
        System.out.println(sb);
    }
}
