import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        int[] nums = {-2,3,0,2,-5};

//        int fst = new fstSolution().solution(nums, nums.length);
        int others = new othersSolution().solution(nums, nums.length);

//        System.out.println("fst = " + fst);
        System.out.println("others = " + others);
    }
}