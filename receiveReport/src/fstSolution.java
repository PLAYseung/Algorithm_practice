import java.util.*;

public class fstSolution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, ArrayList<String>> map = new HashMap<>();
        Map<String , Integer> receive = new HashMap<>();
        int idx = 0;

        for (String id : id_list) {
            ArrayList<String> strings = new ArrayList<>();
            map.put(id,strings);
            receive.put(id,0);
        }

        for (String re : report) {
            String[] users = re.split(" ");

            map.put(users[1], addUSer(map.get(users[1]),users[0]));
        }

        for (ArrayList strings : map.values()) {
            if (strings.size() >= k){
                strings.forEach(user -> receive.put(user.toString(),receive.get(user.toString())+1));
            }
        }

        for (String user: id_list) {
            answer[idx++] = receive.get(user);
        }

        return answer;
    }

    private ArrayList<String> addUSer(ArrayList<String> org, String insertUser){
        org.add(insertUser);
        Set<String> set = new HashSet<>(org);
        ArrayList<String> res = new ArrayList<>(set);
        return res;
    }
}
