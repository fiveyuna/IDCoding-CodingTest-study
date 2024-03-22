import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/* 10818. 최소, 최대
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력) 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
5
20 10 35 30 7

출력) 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
7 35
 */
public class Main {
    public static void main(String args[]) throws IOException {
        
        int N = 0; // 정수의 개수
        int min = Integer.MAX_VALUE; // 최소값
        int max = Integer.MIN_VALUE; // 최대값

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());
        br.close();
        
        for (int i=0; i<N; i++) {
            if (!st.hasMoreTokens()) break;

            // 정수
            int num = Integer.parseInt(st.nextToken());

            if (num > max) max = num;
            if (num < min) min = num;
        }

        // 출력
        System.out.println(min + " " + max);
        return;
    }
}