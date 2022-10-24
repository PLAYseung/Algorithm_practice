import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

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

        List keyList = new ArrayList(clo.keySet());

        for(int i=clo.keySet().size();i>0;i--){
            System.out.println("1관문 통과");
            for(int j = 0 ; j<clo.keySet().size()-i+1 ; j++){
                System.out.println("2관문 진입");
                Object key = keyList.get(j);
                System.out.println(clo.get(key));
            }
        }
        // System.out.println("다시 생각해보자");
        // System.out.println(clo.keySet().size());

        return answer;
    }
}
