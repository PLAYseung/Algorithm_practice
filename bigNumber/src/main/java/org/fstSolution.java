package org;

import java.util.ArrayList;
import java.util.Collections;

public class fstSolution {
    public String solution(int[] numbers) {
        String answer = "";
        ArrayList<String> string_number = new ArrayList<>();

        for (int num:numbers){
            string_number.add(Integer.toString(num));
        }
        // if (Integer.parseInt(answer) < num) {
        //     answer = Integer.toString(num);
        Collections.sort(string_number, Collections.reverseOrder());
        // System.out.println(string_number);
        for (String item:string_number){
            answer += item;
        }

        return answer;
    }
}
