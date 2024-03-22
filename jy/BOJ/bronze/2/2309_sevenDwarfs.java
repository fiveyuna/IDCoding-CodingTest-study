import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;


/* 2309. 일곱 난쟁이
일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

입력) 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
20
7
23
19
10
15
25
8
13

출력) 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
7
8
10
13
19
20
23
 */
public class Main {

    static List<Integer> resultList = null;

    public static void main(String args[]) throws IOException {
        
        //int[] arr = new int[9];
        ArrayList<Integer> list = new ArrayList<>();

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        while ((str = br.readLine()) != null && str.length() > 0) {
            StringTokenizer st = new StringTokenizer(str);

            int n = Integer.parseInt(st.nextToken());

            // 리스트 해당하는 위치에 넣음(정렬)
            int i = 0;
            for (int j=0; j<list.size(); j++) {
                if (list.get(j) < n) {
                    i++;
                }
            }
            list.add(i, n);
        }
        br.close();

        // TODO 드왈프합-100 이 되는 2개를 찾는 로직이 좋은 것 같아요!
        // 조합 찾기
        boolean[] visited = new boolean[list.size()];
        combination(list, visited, 0, list.size(), 7);

        // 출력
        for (int i=0; i<resultList.size(); i++) {
            System.out.println(resultList.get(i));
        }

        return;
    }

    // 백트래킹 사용 조합
    // 사용 예시 : combination(arr, visited, 0, n, r)
    static void combination(List<Integer> list, boolean[] visited, int start, int n, int r) {
        if (r == 0 || resultList != null) {
            int sum = 0;
            ArrayList<Integer> tempList = new ArrayList<>();
            for (int i=0; i<n; i++) {
                if (visited[i]) {
                    tempList.add(list.get(i));
                    sum += list.get(i);
                    if (sum > 100) return;
                }
            }

            if (sum == 100) {
                resultList = tempList;
            }

            return;
        }

        for (int i=start; i<n; i++) {
            visited[i] = true;
            combination(list, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }
}