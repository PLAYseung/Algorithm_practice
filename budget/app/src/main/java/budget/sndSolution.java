package budget;

import java.util.*;

public class sndSolution {
    public int solution(int[] budgets, int M){
        int answer = 0;
        ArrayList<Integer> budgetsList = new ArrayList<>();
        for (int item:budgets){
            budgetsList.add(item);
        }
        
        answer = M/budgets.length;
        
        while (true){
            int exBudget = 0;
            for (int idx=budgetsList.size()-1; -1 < idx; idx--) {
                if (answer > budgetsList.get(idx)) {
                    exBudget += answer-budgetsList.get(idx);
                    budgetsList.remove(idx);
                }
            }

            answer += exBudget/budgetsList.size();
            if (exBudget/budgetsList.size()==0)break;
        }

        return answer;
    }
}
