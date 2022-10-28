public class fstsolution {
    public int solution(int[][] maps) {
		System.out.println(maps.length);
        
        for (int i=0;i<maps.length;i++){
            for (int j=0;j<maps[0].length;j++){
                // 블로그에서 BFS 알고리즘에대한 이해를 하고 난 후 다시 풀어보자
                System.out.print(maps[i][j]);
            }
            System.out.println();
        }

        int answer = 0;
		return answer;
	}
}
