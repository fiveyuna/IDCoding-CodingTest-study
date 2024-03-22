import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/* 10870. 피보나치 수 5
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력) 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
10

출력) 첫째 줄에 n번째 피보나치 수를 출력한다.
55
 */
public class Main {
    public static void main(String args[]) throws IOException {
        
        int n = 0; // n번째
        int a = 0; // 0번째 피보나치 수
        int b = 1; // 1번째 피보나치 수

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken().trim());
        br.close();
        
        if (n == 0) {
            System.out.println(a);
        } else {
            for (int i=1; i<n; i++) {
    
                int num = a + b;
                a = b;
                b = num;
            }
            System.out.println(b);
        }

        return;
    }
}