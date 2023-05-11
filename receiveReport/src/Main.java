public class Main {
    public static void main(String[] args) {
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};

        String[] id_list_2 = {"con", "ryan"};
        String[] report_2 = {"ryan con", "ryan con", "ryan con", "ryan con"};

        int k = 2;
        int k_2 = 3;

        int[] fst = new otherSolution().solution(id_list, report, k);
        int[] snd = new otherSolution().solution(id_list_2, report_2, k_2);
//        int[] fst = new fstSolution().solution(id_list, report, k);
//        int[] snd = new fstSolution().solution(id_list_2, report_2, k_2);

        for (int i : fst) {
            System.out.print("fst = " + i + " / ");
        }
        System.out.println();
        for (int i : snd) {
            System.out.print("snd = " + i + " / ");
        }
    }
}