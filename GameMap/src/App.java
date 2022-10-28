public class App {
    public static void main(String[] args) throws Exception {
        int[][] maps = {
            {1,0,1,1,1},
            {1,0,1,0,1},
            {1,0,1,1,1},
            {1,1,1,0,1},
            {0,0,0,0,1}
        };

        fstsolution fstsol = new fstsolution();

        System.out.println(fstsol.solution(maps));
    }
}
