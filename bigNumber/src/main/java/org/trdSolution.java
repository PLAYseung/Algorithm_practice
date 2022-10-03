package org;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.*;

public class trdSolution {
    public String solution(int[] numbers) {
        
        // 최종적인 형태
        // 자바의 라이브러리 활용
        String answer = IntStream.of(numbers)
            .mapToObj(String::valueOf)
            .sorted((s1,s2) -> (s2+s1).compareTo(s1+s2))
            .collect(Collectors.joining());

        // String[] strNums = new String[numbers.length];
        // for (int i=0; i<numbers.length; i++ ){
        //     strNums[i] = "" + numbers[i];
        // }

        // // 기존의 형태
        // // Arrays.sort(strNums, new Comparator<String>() {
        // //     public int compare(String s1,String s2) {
        // //         return (s2+s1).compareTo(s1+s2);
        // //     }
        // // });

        // // 람다식으로 변형
        // Arrays.sort(strNums, (s1, s2) -> (s2+s1).compareTo(s1+s2));
    
        // String answer = "";
        
        // for (String s : strNums){
        //     answer += s;
        // }

        // 권장되는 형태
        if(answer.startsWith("0")) return "0";

        return answer;
    }
}
