public class App {
    public static void main(String[] args) throws Exception {
        String[][] clothes = new String[][]{
            {"yellowhat", "headgear"}, 
            {"bluesunglasses", "eyewear"}, 
            {"green_turban", "headgear"}};

        // fstsolution fstsol = new fstsolution();
        // sndsolution sndsol = new sndsolution();
        // trdsolution trdsol = new trdsolution();
        fthsolution fthsol = new fthsolution();

        // System.out.println(fstsol.solution(clothes));
        // System.out.println(sndsol.solution(clothes));
        System.out.println(fthsol.solution(clothes));
    }
}
