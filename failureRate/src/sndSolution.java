import java.util.ArrayList;
import java.util.Collections;

public class sndSolution {

    int[] solution(int N, int[] stages){

        int[] answer = new int[N];
        double[] stage = new double[N+1];

        for (int i : stages){
            if (i == N+1){
                continue;
            }

            stage[i]++;
        }

        ArrayList<Double> fail = new ArrayList<>();

        // 스테이지에 도달한 명수
        double num = stages.length;
        // 다음 스테이지로 올라갈때 줄어드는 사용자 수를 계산하기 위해서 사용
        double tmp = 0;

        for (int i = 1; i<stage.length; i++) {
            // 도달한 사용자가 0명이면 실패율도 0
            tmp = stage[i];
            if(num == 0){
                stage[i] = 0;
            } else {
                stage[i] = stage[i]/num;
                num = num - tmp;
            }
            fail.add(stage[i]);
        }
        // fail을 내림차순 정렬
        Collections.sort(fail, Collections.reverseOrder());

        // 정렬된 fail 리스트 값과 stage값을 비교해서 같으면 stage의 인덱스번호를 가져와서 실패율이 높은 순으로 answer배열에 넣어준다
        for (int i=0; i<fail.size(); i++){
            for(int j=1; j<stage.length; j++){
                if(fail.get(i) == stage[j]){
                    answer[i] = j;
                    stage[j]=-1;
                    break;
                }
            }
        }

        return answer;
    }

}
