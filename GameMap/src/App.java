public class App {
    public static void main(String[] args) throws Exception {
        int[][] maps = {
            {1,0,1,1,1},
            {1,0,1,0,1},
            {1,0,1,1,1},
            {1,1,1,0,1},
            {0,0,0,0,1}
        };

        // fstsolution fstsol = new fstsolution();
        sndsolution sndsol = new sndsolution();

        // System.out.println(fstsol.solution(maps));
        System.out.println(sndsol.solution(maps));
    }
}
