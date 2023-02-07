public class Main {
    public static void main(String[] args) {
        String[] survey = {"AN", "CF", "MJ", "RT", "NA"};
        int[] choices = {5, 3, 2, 7, 5};

        String fst = new fstSolution().solution(survey, choices);
        String other = new otherSolution().solution(survey, choices);

        System.out.println("fst = " + fst);
        System.out.println("other = " + other);
    }
}