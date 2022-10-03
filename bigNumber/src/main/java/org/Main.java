package org;

public class Main {
    public static void main(String[] args) {

        int[] testList = new int[5];
        testList[0] = 3;
        testList[1] = 30;
        testList[2] = 34;
        testList[3] = 5;
        testList[4] = 9;
        
        fstSolution fstsol = new fstSolution();

        System.out.println(fstsol.solution(testList));

    }
}