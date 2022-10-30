import java.util.LinkedList;
import java.util.Queue;

public class sndsolution {

    class Position {
        int x,y;

        Position(int x, int y){
            this.x = x;
            this.y = y;
        }

        boolean isValid(int width, int height){
            if(x < 0 || x >= width) return false;
            if(y < 0 || y >= height) return false;
            return true;
        }
    }

    public int solution(int[][] maps) {
        // BFS : Queue

        int mapHeight = maps.length;
        int mapWidth = maps[0].length;

        Queue<Position> queue = new LinkedList<>();
        int[][] count = new int[mapHeight][mapWidth];
        boolean[][] visited = new boolean[mapHeight][mapWidth];

        // 큐에 값을 넣는 것 : offer
        queue.offer(new Position(0,0)); // 최초 시작 값
        count[0][0] = 1;
        visited[0][0] = true;

        while(!queue.isEmpty()){ // 큐가 빌대 까지
            //큐에서 값을 꺼내오는 것 : poll
            Position current = queue.poll(); // 현재 위치를 꺼내옴

            int currentCount = count[current.y][current.x];

            // 4가지 경우
            // 이동 가능한 모든 경우의 수 계산
            final int[][] moving = {{0,-1},{0,1},{-1,0},{1,0}};
            for(int i=0;i<moving.length;i++){
                Position moved = new Position(current.x+moving[i][0],current.y+moving[i][1]);
                if(!moved.isValid(mapWidth, mapHeight)) continue;
                if(visited[moved.y][moved.x]) continue;
                if(maps[moved.y][moved.x]==0) continue; // 0 : 벽, 1 : 길

                count[moved.y][moved.x] = currentCount +1;
                visited[moved.y][moved.x] = true;
                queue.offer(moved); // 계산된 것을 다시 큐에 삽입
            }

        }

        int answer = count[mapHeight-1][mapWidth-1]; // 모든 위치를 탐색 했을 때의 마지막 위치
        if(answer == 0) return -1;
		return answer;
	}
}
