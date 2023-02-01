import java.util.HashMap;
import java.util.Map;

public class othersSolution {
    public int[] solution(int[] lottos, int[] win_nums){
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        int zeroCount = 0;

        for(int lotto : lottos) {
            if(lotto == 0) {
                zeroCount++;
                continue;
            }
            map.put(lotto, true);
        }


        int sameCount = 0;
        for(int winNum : win_nums) {
            // map에 해당하는(winNum) 값을 키로 가지고 있는지 ~= containsValue()
            // list의 contains를 사용하는 것은 어떤가?
            if(map.containsKey(winNum)) sameCount++;
        }

        int maxRank = 7 - (sameCount + zeroCount);
        int minRank = 7 - sameCount;
        if(maxRank > 6) maxRank = 6;
        if(minRank > 6) minRank = 6;

        return new int[] {maxRank, minRank};
    }
}
