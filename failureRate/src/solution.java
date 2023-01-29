import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class solution {
    public int[] solution(int N, int[] lastStages) {
        int nPlayers = lastStages.length;
        int[] nStagePlayers = new int[N + 2];
        // 몇번째 스테이지에 몇명이 있는지 알 수 있다
        for (int stage : lastStages) {
            nStagePlayers[stage] += 1;
        }

        // 몇명의 플레이어가 남아 있는지 확인 하기 위한 변수
        // 전체 플레이어 수 만큼 값을 가진다
        int remainingPlayers = nPlayers;

        // 스테이지를 각각의 객체로 만들어서 배열에 저장하기 위한 배열
        List<Stage> stages = new ArrayList<>();

        // 스테이지 1부터 실패율을 계산하고 객체를 생성하는 로직
        for (int id = 1 ; id <= N; id++) {
            double failure = (double) nStagePlayers[id] / remainingPlayers;
            remainingPlayers -= nStagePlayers[id];

            Stage s = new Stage(id, failure);

            // 생성한 객체를 배열에 등록
            stages.add(s);
        }

        // 클래스 배열 정렬
        Collections.sort(stages, Collections.reverseOrder());

        // 정렬된 객체의 id 값을 반환받아서 결과 배열에 전달
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = stages.get(i).id;
        }
        return answer;
    }

    // 객체를 배열로 만들어 정렬하기 위해 Comparable<> 상속
    class Stage implements Comparable<Stage> {
        public int id;
        public double failure;

        public Stage(int id_, double failure_) {
            id = id_;
            failure = failure_;
        }

        // Comparable<> 이 가지고 있는 메서드를 정의
        @Override
        public int compareTo(Stage o) {
            if (failure < o.failure ) {
                return -1;
            }
            if (failure > o.failure ) {
                return 1;
            }
            return 0;
        }
    }

}
