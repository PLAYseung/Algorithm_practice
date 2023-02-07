public class fstSolution {

    int[][] hand = {{3, 0},{3, 2}};
    public String solution(int[] numbers, String hand){

        String use = hand.toUpperCase().substring(0,1);
        int mainHand = use.equals("L") ? 0 : 1;
        String answer = "";

        for (int number : numbers) {
            int[] pos = new int[2];

            if (number == 0){
                pos[0] = 3; pos[1] = 1;
            } else {
                number -= 1;
                pos[0] = number/3;
                pos[1] = number%3;
            }

            answer += pos[1]==0 ? moveLeft(pos) : pos[1]==2 ? moveRight(pos) : result(pos,mainHand,use);

        }

        return answer;
    }

    String moveLeft(int[] point){ this.hand[0] = point; return "L";}
    String moveRight(int[] point){ this.hand[1] = point; return "R";}

    String result(int[] point, int mainHand,String use){

        int lLong = Math.abs(point[0]-hand[0][0]) + Math.abs(point[1]-hand[0][1]);
        int rLong = Math.abs(point[0]-hand[1][0]) + Math.abs(point[1]-hand[1][1]);

        if(lLong < rLong) {
            this.hand[0] = point;
            return "L";
        } else if(rLong < lLong) {
            this.hand[1] = point;
            return "R";
        } else {
            this.hand[mainHand] = point;
            return use;
        }
    }
}
