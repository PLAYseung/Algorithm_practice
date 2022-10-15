public class App {
    public static void main(String[] args) throws Exception {

        int[] A = new int[4];
        int[] B = new int[4];

        A[0] = 5;
        A[1] = 1;
        A[2] = 3;
        A[3] = 7;
        
        B[0] = 2;
        B[1] = 2;
        B[2] = 6;
        B[3] = 8;

        // fstsolution fstsol = new fstsolution();
        // sndsolution sndsol = new sndsolution();
        trdsolution trdsol = new trdsolution();

        // System.out.println(fstsol.solution(A, B));
        // System.out.println(sndsol.solution(A, B));
        System.out.println(trdsol.solution(A, B));
    }
}
