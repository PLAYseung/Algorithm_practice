import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class sndsolution {
    public int solution(String[][] clothes) {
        Map<String,Integer> clo = new HashMap<String,Integer>();

        for (String[] clothe : clothes) {
            if (clo.get(clothe[1]) == null){
                clo.put(clothe[1], 1);
            } else {
                clo.put(clothe[1],clo.get(clothe[1])+1);
            }
        }

        List keyList = new ArrayList(clo.keySet());

        if (keyList.size()==1){
            return clo.get(keyList.get(0));
        }

        int sum=0;
        for (int i = 0; i<keyList.size(); i++){
            int mul=1;
            int mul_j_sum=0;
            int mul_sum=0;
            for(int j = 0; j<keyList.size(); j++){
                for(int k=0; k<i;k++){
                    mul = clo.get(keyList.get(j));
                    System.out.println(mul);
                    int mul_j=0;
                    if(keyList.size()-j<i+j-1){
                        System.out.println(" in this");
                        for(int l=1; l<=keyList.size()-j;l++){
                            mul_j += (mul * clo.get(keyList.get(j+l)));
                        }
                    }else{
                        mul_j += mul;
                    }
                    mul_j_sum += mul_j;
                }
                mul_sum += mul_j_sum;
            }
            sum += mul_sum;
        }

        return sum;
    }
}
