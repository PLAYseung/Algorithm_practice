public class Main {
    public static void main(String[] args) {

        int[] numbers = {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2};
        String hand = "left";

        String fst = new fstSolution().solution(numbers, hand);

        System.out.println("fst = " + fst);
    }
}