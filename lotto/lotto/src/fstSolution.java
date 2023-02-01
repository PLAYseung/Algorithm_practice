public class fstSolution {

    private int rank(int num){
        if (num==6){
            return 1;
        } else if (num==5) {
            return 2;
        } else if (num==4) {
            return 3;
        } else if (num==3) {
            return 4;
        } else if (num==2) {
            return 5;
        }
        return 6;
    }
    public int[] solution(int[] lottos, int[] win_nums){

        int cnt = 0;
        int zero_cnt = 0;

        for (int item : lottos){
            if (item==0){
                zero_cnt++;
            }
        }

        for (int i=0; i<6; i++){
            for (int j=0; j<6; j++){
                if (win_nums[i]==lottos[j]){
                    cnt++;
                }
            }
        }

        int[] ans = new int[2];
        System.out.println(zero_cnt + ", " + cnt);
        ans[0] = rank(zero_cnt+cnt);
        ans[1] = rank(cnt);

        return ans;
    }
}
