import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class fstSolution {
    int[] solution(int N, int[] stages){

        float[] clear = new float[N];
        float[] rates = new float[N];
        int[] result = {};
        int players = stages.length;

        for (int stage : stages){
            if (stage < N) {
                clear[stage-1]++;
            }
        }

        for (int i=0 ; i<clear.length ; i++ ){
            rates[i] = clear[i] / players;
            players -= clear[i];
        }

        for (int i=0 ; i<rates.length ; i++ ) {
            float comNum = 0;
            int idx = 0;
            for (int j=0 ; j<rates.length ; j++) {
                if (comNum < rates[j]) {
                    comNum = rates[j];
                    result = AddList(result,i,j+1);
                    idx = j;
                }
            }
            rates[idx]=-1;
            System.out.println(result.length);
        }

        for (int i=0 ; i<rates.length ; i++) {
            for (int j=0 ; j<rates.length ; j++) {
                if (rates[j]==0) {
                    result = AddList(result,result.length,j+1);
                    rates[j] = -1;
                }
            }
        }

        return result;
    }

    int[] AddList(int[] list, int len, int num){
        int[] newList = new int[len+1];
        for (int i=0; i<len; i++) {
            newList[i]=list[i];
        }
        newList[len]=num;
        return newList;
    }
}
