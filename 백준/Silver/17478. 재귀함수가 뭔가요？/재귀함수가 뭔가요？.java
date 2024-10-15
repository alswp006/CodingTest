import java.io.*;

public class Main {
    public static void printUnderbar(BufferedWriter bw, int num) throws IOException {
        for (int i = 0; i < num; i++){
            bw.write("____");
        }
    }

    public static void deep(BufferedWriter bw, int depth, int result) throws IOException {
        if (depth == result) {
            printUnderbar(bw, depth);
            bw.write("\"재귀함수가 뭔가요?\"\n");
            printUnderbar(bw, depth);
            bw.write("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
            printUnderbar(bw, depth);
            bw.write("라고 답변하였지.\n");
            return;
        }

        printUnderbar(bw, depth);
        bw.write("\"재귀함수가 뭔가요?\"\n");
        printUnderbar(bw, depth);
        bw.write("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
        printUnderbar(bw, depth);
        bw.write("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
        printUnderbar(bw, depth);
        bw.write("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");

        deep(bw, depth + 1, result);

        printUnderbar(bw, depth);
        bw.write("라고 답변하였지.\n");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        bw.write("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");

        deep(bw, 0, n);

        bw.flush();  // 출력 버퍼 비우기
        bw.close();  // BufferedWriter 닫기
        br.close();  // BufferedReader 닫기
    }
}