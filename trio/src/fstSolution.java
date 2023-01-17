public class fstSolution {

    int solution(int number[], int number_len) {

        int start = 0;
        int sumNum;
        int result = 0;

        while (start < number_len-2) {
            for (int i=start+1; i<number_len-1; i++) {
                for (int j=i+1; j<number_len; j++) {
                    sumNum = number[start] + number[i] + number[j];

                    if (sumNum==0) {
                        result++;
                    }
                }
            }
            start++;
        }

        return result;
    }

}
