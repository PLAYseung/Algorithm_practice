import java.util.Arrays;

public class fstsolution {
    public int solution(int[] A, int[] B) {

        int amax = 0;
        int amin = 1000000000;
        int bmax = 0;
        int bmin = 1000000000;
        int cnt = 0;

        for (int numA : A) amax = Math.max(numA, amax);
        for (int numA : A) amin = Math.min(numA, amin);

        for (int numB : B) bmax = Math.max(numB, bmax);
        for (int numB : B) bmin = Math.min(numB, bmin);

        if (bmin > amax) return B.length;
        if (amin > bmax) return 0;

        Arrays.sort(A);
        Arrays.sort(B);

        int i = 0;

        for (int a : A) {
            for (; i < B.length ; i++) {
                if (B[i] > a) {
                    System.out.println(B[i]);
                    i++;
                    cnt++;
                    break;
                }
            }
        }

        return cnt;
    }
}
