import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer st = new StreamTokenizer(System.in);
        StringBuilder sb = new StringBuilder();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st.nextToken();
        int n = (int)st.nval;
        for(int i = 0; i < n; i++) {
            st.nextToken();
            int a = (int)st.nval;
            st.nextToken();
            int b = (int)st.nval;
            sb.append(a + b).append('\n');
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}