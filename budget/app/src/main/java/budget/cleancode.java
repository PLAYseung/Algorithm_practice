package budget;

import java.util.stream.*;

public class cleancode {
    public int solution(int[] budgets, int M){

        int min = 0;
        int max = IntStream.of(budgets).max().orElse(0);
        // Stream 으로 요약
        // for (int b:budgets){
        //     if(b>max) max=b;
        // }

        int answer = 0;
        while(min <= max){
            final int mid = (min + max) / 2; // 가변 인수 사용 방지

            int sum = IntStream.of(budgets)
                .map( b -> Math.min(b, mid)) // 가변 인수 사용 X
                .sum();
            // int sum = 0;
            // for (int b:budgets){
            //     if(b > mid) sum += mid;
            //     else sum += b;
            // }

            if(sum <= M) {
                min = mid + 1;
                answer = mid;
            } else {
                max = mid -1;
            }
        }
        
        return answer;
    }
}
