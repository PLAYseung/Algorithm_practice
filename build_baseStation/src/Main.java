import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Integer> station = new ArrayList<Integer>();
        station.add(4);
        station.add(11);
    
        Solution sol = new Solution();

        sol.solution(11, station, 1);

    }
}