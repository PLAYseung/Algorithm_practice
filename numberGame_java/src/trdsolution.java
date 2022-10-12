import java.util.Arrays;

public class trdsolution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);
        int index = B.length-1;

        int answer = 0;
        // 2중 루프를 루프 1개로
        for (int i=A.length; i>=0; i--) {
            // 서로 큰값을 비교해가면서 진행되는 방식
            if (A[i] < B[index]){
                index--;
                answer++;
            }
        }
        return answer;
    }
}