public class Main {
    public static void main(String[] args) {

        int m = 2;
        int n = 5;
        
        int fst = new fstSolution().solution(m,n);

        System.out.println("fst = " + fst);

        // 걍 곱합기 -1 하면됨... 뭐한거임?
        System.out.println(m*n-1);
    }
}