public class Main {
    public static void main(String[] args) {

        int N = 5;
        int[] stages = {2,1,2,6,2,4,3,3};

//        int[] fst = new fstSolution().solution(N,stages);
        int[] snd = new sndSolution().solution(N,stages);

//        for (int num : fst){
//            System.out.println("num = " + num);
//        }
        for (int num : snd){
            System.out.println("num = " + num);
        }
    }
}