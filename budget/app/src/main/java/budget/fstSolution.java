package budget;

public class fstSolution {
    public int solution(int[] budgets, int M){
        int answer = 0;
        int exBudget = 0;
        int len_budgets = budgets.length;

        answer = M/budgets.length;
        for (int item : budgets) {
            if (answer > item) {
                exBudget += answer-item;
                len_budgets -= 1;
            }
        }

        answer += exBudget/len_budgets;

        return answer;
    }
}
