import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class otherSolution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // report에서 중복을 제거 -> 같은 사용자가 여러번 신고하는 것 방지
        List<String> list = Arrays.stream(report).distinct().collect(Collectors.toList());
        // 사용자가 받는 신고 횟수
        HashMap<String, Integer> count = new HashMap<>();

        for (String s : list) {
            // 신고 받는 사용자에 +1
            String target = s.split(" ")[1];
            // .getOrDefault : .get 동작을 하거나 키값이 없다면 기본값을 반환
            count.put(target, count.getOrDefault(target, 0) + 1);
        }

        // id_list를 스트림
        return Arrays.stream(id_list).map(_user -> {
            // .map : id_list의 각요소들을 조건에 해당 하는 값으로 변환
            // user의 값이 변하지 않게 final 선언
            final String user = _user;
            // .filter : 요소들을 조건에 따라 걸러내는 작업
            // .startWith : 주어진 요소로 시작하는 지 ( true / false )
            // .collect : 스트림의 최종연산, 매개변수로 컬렉터를 필요로 한다
            // reportList의 형태 : "신고자 사용자"의 형태중 신고자가 일치하는 문자열만 있는 리스트
            List<String> reportList = list.stream().filter(s -> s.startsWith(user + " ")).collect(Collectors.toList());
            // .count : stream 실행시 조건에 해당하는 요소들의 갯수 반환
            // reportList에서 가지고 있는 문자열을 각각 실행
            // "신고자 사용자"에서 사용자의 값을 count에서 받아서 k값과 비교하고 k값을 넘는 것들만 갯수를 셈
            return reportList.stream().filter(s -> count.getOrDefault(s.split(" ")[1], 0) >= k).count();
        // .mapToInt : 스트림을 intStream으로 변환해주는 메서드
        }) // :: (이중 콜론 연산자) : 매개변수의 반복 사용을 줄여줌
//                .toArray() : 배열로 변환 해줌
//                .mapToInt(x->x.intValue()).toArray();
                .mapToInt(Long::intValue).toArray();
    }
}
