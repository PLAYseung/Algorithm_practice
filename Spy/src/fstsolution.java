import java.util.HashMap;
import java.util.Map;

public class fstsolution {
    public int solution(String[][] clothes) {
        int answer = 0;

        Map<String,Integer> clo = new HashMap<String,Integer>();

        for (String[] clothe : clothes) {
            if (clo.get(clothe[1]) == null){
                clo.put(clothe[1], 1);
            } else {
                clo.put(clothe[1],clo.get(clothe[1])+1);
            }
        }

        System.out.println("다시 생각해보자");

        return answer;
    }
}
