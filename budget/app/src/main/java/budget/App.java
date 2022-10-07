package budget;

public class App {
    public static void main(String[] args) {
        int[] budgets = new int[4];
        budgets[0] = 120;
        budgets[1] = 110;
        budgets[2] = 140;
        budgets[3] = 150;

        int M = 485;

        // fstSolution fstSol = new fstSolution();
        // sndSolution sndSol = new sndSolution();
        // trdSolution trdSol = new trdSolution();
        cleancode clcode = new cleancode();

        // System.out.println(fstSol.solution(budgets,M));
        // System.out.println(sndSol.solution(budgets,M));
        // System.out.println(trdSol.solution(budgets,M));
        System.out.println(clcode.solution(budgets,M));
    }
}
