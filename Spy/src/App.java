public class App {
    public static void main(String[] args) throws Exception {
        String[][] clothes = new String[][]{
            {"yellowhat", "headgear"}, 
            {"bluesunglasses", "eyewear"}, 
            {"green_turban", "headgear"}};

        fstsolution fstsol = new fstsolution();

        System.out.println(fstsol.solution(clothes));
    }
}
