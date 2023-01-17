import java.util.Stack;
import java.util.Scanner;
import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        ArrayList<Stack> stackList = new ArrayList<>();
        int caseNum = sc.nextInt();
        for (int i=0 ; i<caseNum ; i++){
            int inputNumSize = sc.nextInt();
            Stack<Integer> stack = new Stack<>();
            int caseNumbers = sc.nextInt();
            for (int j=0 ; i<inputNumSize ; j++)
                stack.push(caseNumbers);
            stackList.add(stack);
        }
        System.out.println(stackList);

    }
}
