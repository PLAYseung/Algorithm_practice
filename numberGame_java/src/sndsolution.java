import java.util.Arrays;

public class sndsolution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(B);

        int answer = 0;
        // 2중 루프
        for (int i=0; i<A.length; i++){
            for (int j=0; j<B.length; j++) {
                if (A[i] < B[j]) {
                    answer++;
                    B[j] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}