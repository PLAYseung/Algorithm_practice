public class fstSolution {

    int solution(String s) {

        String[] words = {"zero","one","two","three","four","five","six","seven","eight","nine"};

        for (int i=0; i<words.length; i++) {
            s = s.replace(words[i], String.valueOf(i));
        }

        return Integer.parseInt(s);
    }
}
