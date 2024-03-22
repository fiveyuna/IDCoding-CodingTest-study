import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/* 2460. 지능형 기차 2 
10개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.

입력) 각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 열 번째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 
0 32
3 13
28 25
17 5
21 20
11 0
12 12
4 2
0 8
21 0

출력) 첫째 줄에 최대 사람 수를 출력한다.  
42
 */
public class Main {
    public static void main(String args[]) throws IOException {
        
        int num = 0; // 기차에 탄 사람 수
        int max = 0; // 기차에 사람이 가장 많을 때의 사람 수

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp;
        StringTokenizer st;

        while((tmp = br.readLine())!= null && (st = new StringTokenizer(tmp)) != null && st.countTokens() > 0) {
            int off = Integer.parseInt(st.nextToken()); // 내린 사람 수
            int on = Integer.parseInt(st.nextToken()); // 탄 사람 수

            num = num - off + on;

            if (num > max) max = num;
        }
        br.close();

        // 출력
        System.out.println(max);
        return;
    }
}