import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution{
    
    public int solution(int n, int[] station, int w) {
        int answer = 3;

        int[] emptyList = new int[n];
        Arrays.fill(emptyList,0);
        
        // System.out.println(emptyList);
        
        for (Integer item:station){
            System.out.println(item);
            // System.out.println((emptyList[item-1]));
            emptyList[item-1]++;
        }
        
        System.out.println(Arrays.toString(emptyList));
        
        return answer;
    }
}
