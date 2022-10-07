package budget;

import java.util.*;

public class trdSolution {
    public int solution(int[] budgets, int M){

        int min = 0;
        int max = 0;
        for (int b:budgets){
            if(b>max) max=b;
        }

        int answer = 0;
        while(min <= max){
            int mid = (min + max) / 2;

            int sum = 0;
            for (int b:budgets){
                if(b > mid) sum += mid;
                else sum += b;
            }

            if(sum <= M) {
                min = mid + 1;
                answer = mid;
            } else {
                max = mid -1;
            }
            System.out.println("min : "+ min);
            System.out.println("max : "+ max);
            System.out.println("mid : "+ mid);
            System.out.println("sum : "+ sum);
            System.out.println("- - - - - - - - - - - - - - - - -");
        }
        
        return answer;
    }
}
