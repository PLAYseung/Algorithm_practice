import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // ArrayList<Integer> station = new ArrayList<Integer>();
        // station.add(4);
        // station.add(11);
        int[] station = new int[2];
        station[0] = 4;
        station[1] = 11;

        // Solution sol = new Solution();
        sndSolution sndsol = new sndSolution();

        // System.out.println(sol.solution(11, station, 1));
        System.out.println(sndsol.solution(11, station, 1));

    }
}