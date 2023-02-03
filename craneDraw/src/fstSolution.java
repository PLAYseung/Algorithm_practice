import java.util.ArrayList;

public class fstSolution {
    public int solution(int[][] board, int[] moves){

        ArrayList<Integer> getNum = new ArrayList<>();

        for (int num : moves) {
            for (int idx=0; idx<board.length; idx++){
                if (board[idx][num-1]!=0){
                    getNum.add(board[idx][num-1]);
                    board[idx][num-1]=0;
                    break;
                }
            }
        }

        int org = 0;
        int finish=getNum.size()-1;

        while (true) {
            int com = org;
            for (int idx=0; idx<finish; idx++) {
                if (getNum.get(idx) == getNum.get(idx+1)){
                    boolean re = getNum.get(idx) == getNum.get(idx+1);
                    org+=2;
                    getNum.remove(idx);
                    getNum.remove(idx);
                    finish-=2;
                    break;
                }
            }
            if (com==org){
                break;
            }
        }
        return org;
    }
}
