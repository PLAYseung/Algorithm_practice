import java.util.HashMap;
import java.util.Map;

public class trdsolution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> counts = new HashMap<>();

        for(String[] c : clothes){
            String type = c[1]; // 옷의 종류
            counts.put(type, counts.getOrDefault(type, 0)+1); // 키값을 확인 후 증가 시키는 함수
        }

        for (Integer c:counts.values()){
            System.out.println(c);
            answer *= c+1; // 사용하지 않은 경우를 더해줌
        }
        
        answer -= 1; // 모든 용품을 사용하지 않는 경우의 수

        return answer;
    }
}
