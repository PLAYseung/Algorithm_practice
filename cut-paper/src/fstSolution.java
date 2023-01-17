public class fstSolution {

    int solution(int M, int N) {

        if (M==1 && N==1) {
            return 0;
        } else if (M > N) {
            return cal(M,N);
        } else {
            return cal(N,M);
        }

    }

    int cal(int bigNum, int smallNum) {

        int fstCut = bigNum - 1;
        int sndCut = smallNum -1;

        return fstCut + bigNum*sndCut;

    }
}
