import java.io.*;
import java.util.*;

// 2501. 약수 구하기
public class Main {
    public static void main(String args[]) throws IOException {
        
        int N = 0;
        int K = 0;
        int result = 0;

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        

        // @ N의 약수 구하기
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i=1; i<=Math.sqrt(N); i++) {
            if (N % i == 0) {
                list.add(i);
                if (N/i != i) {
                    list.add(N/i);
                }
            }
        }

        // @ 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력
        // @ N의 약수들 중 K번째로 작은 수 출력
        if (list.size() >= K) {
            // 정렬
            Collections.sort(list);
            result = list.get(K - 1);
        }

        // 출력
        System.out.println(result);

        return;
    }
}