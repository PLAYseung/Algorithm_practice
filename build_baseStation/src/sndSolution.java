import java.util.*;

public class sndSolution {
    public int solution(int n, int[] stations, int w){
        int answer = 0;
        int si = 0;
        int position = 1;

        while (position <= n){
            if(si < stations.length && stations[si] - w <= position){
                position = stations[si] + w + 1;
                si += 1;
            } else {
                answer += 1;
                position += w * 2 + 1; 
            }
        }

        return answer;
    }
}
