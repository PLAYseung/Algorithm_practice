public class othersSolution {

    static int ans[] = new int[3];
    static int numArr[];
    static int N;
    static int resultCount = 0;

    int solution(int number[], int number_len) {
        this.numArr = number;
        this.N = number_len;

        // 재귀함수를 이용한 풀이
        DFS(0,0);
        return resultCount;
    }

    private void DFS(int idx, int depth) {
        if (depth == 3) {
            int sum = 0;
            for (int i=0; i<3; i++) {
                sum += ans[i];
            }

            if (sum == 0) {
                resultCount++;
            }

            System.out.println("idx : " + idx + " | " + "depth : " +depth);
            return;
        }

        // depth가 3미만 일때
        for (int i=idx; i<N; i++) {
            ans[depth] = numArr[i];
            System.out.println("i : " + i + " | " + "depth : " +depth);
            DFS(i+1, depth+1);
        }
    }
}
