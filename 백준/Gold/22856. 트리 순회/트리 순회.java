import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int answer;
    static int n;
    static int[][] tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        boolean[] isRoot = new boolean[n + 1];
        boolean[] visited = new boolean[n + 1];
        isRoot[0] = true;
        tree = new int[n + 1][2];

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            tree[parent][0] = left;
            tree[parent][1] = right;
            if(left != -1) isRoot[left] = true;
            if(right != -1)isRoot[right] = true;
        }

        int root_node = 0;
        for(int i = 0; i < n + 1; i++){
            if (!isRoot[i]){
                root_node = i;
                break;
            }
        }
        dfs(root_node, visited);
        visited = new boolean[n + 1];
        dfs_right(root_node, visited);


        System.out.println(answer - 1);
    }

    static void dfs(int node, boolean[] visited){
        if (visited[node]) return;
        visited[node] = true;
        if (tree[node][0] != -1)  dfs(tree[node][0], visited);
        if (tree[node][1] != -1)  dfs(tree[node][1], visited);
        answer += 2;
    }

    static void dfs_right(int node, boolean[] visited){
        if (visited[node]) return;
        visited[node] = true;
        if (tree[node][1] != -1)  dfs_right(tree[node][1], visited);
        answer -= 1;
    }
}
