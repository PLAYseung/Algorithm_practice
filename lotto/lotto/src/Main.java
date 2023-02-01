import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
//        int[] lottos = {45, 4, 35, 20, 3, 9};
//        int[] win_nums = {20, 9, 3, 45, 4, 35};
//
//        int[] fst = new fstSolution().solution(lottos, win_nums);
//
//        for (int num : fst){
//            System.out.print(num + "\t");
//        }
        long count = IntStream.of(1, 3, 5, 7, 9).count();
        System.out.println("count = " + count);

    }
}