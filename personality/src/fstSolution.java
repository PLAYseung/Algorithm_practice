import java.util.HashMap;
import java.util.Map;

public class fstSolution {

    Map<Character, Integer> personal = new HashMap<>();
    char[][] personalitySet = {{'R', 'T'}, {'C','F'}, {'J','M'}, {'A','N'}};

    public String solution(String[] survey, int[] choices){

        // 값 저장하기 위한 Map 생성
        for ( char[] each : personalitySet ) {
            this.personal.put(each[0],0);
            this.personal.put(each[1],0);
        }

        for (int i = 0; i < survey.length; i++) {
            compare(survey[i],choices[i]);
        }

        String answer="";

        for (char[] t: personalitySet ) {

//            char fst = t[0];
//            char snd = t[1];
//            if (personal.get(snd) > personal.get(fst)){
//                answer += snd;
//            } else {
//                answer += fst;
//            }
//          삼항 연산자식으로 표현
            answer += this.personal.get(t[1]) > this.personal.get(t[0]) ? t[1] : t[0];
        }

        return answer;
    }

    private void compare(String st, int i) {
        char fst = st.charAt(0);
        // char -> String 으로 변환하는 방법
        // String snd = String.valueOf(st.charAt(0));
        char snd = st.charAt(1);

        if (i-4 > 0){
            this.personal.put(snd,this.personal.get(snd)+(i-4));
        } else if (i-4 < 0){
            this.personal.put(fst,this.personal.get(fst)+(4-i));
        }
    }

}
