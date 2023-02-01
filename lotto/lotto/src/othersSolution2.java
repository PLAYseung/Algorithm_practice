import java.util.Arrays;
import java.util.stream.LongStream;

public class othersSolution2 {
    public int[] solution(int[] lottos, int[] winNums){
        // 쉽게 난수 스트림을 생성해서 여러가지 후속 작업을 취할 수 있어 유용
        return LongStream.of(
                // 7 - 같은 숫자 갯수 + 0의 갯수
                // 7 - 같은 숫자 갯수
                // Arrays.stream : int 배열을 스트림 배열로 변환
                // .filter() : 스트림 내의 요소들을 하나씩 평가 해서 걸러내는 작업
                // .anyMatch() : 하나라도 조건을 만족하는 요소가 있는지
                        (lottos.length + 1) - Arrays.stream(lottos).filter(l -> Arrays.stream(winNums).anyMatch(w -> w == l) || l == 0).count(),
                        (lottos.length + 1) - Arrays.stream(lottos).filter(l -> Arrays.stream(winNums).anyMatch(w -> w == l)).count()
                )
                // mapToInt() : longStream 을 IntStream 으로 변환 해주는 메서드
                // 같은 것이 하나도 존재하지 않고 0이 없을 때를 위한 조건
                .mapToInt(op -> (int) (op > 6 ? op - 1 : op))
                // toArray() : 스르림을 다시 배열로 변환하는 메서드
                .toArray();
    }
}
