import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/* 2609. 최대공약수 최소공배수
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력) 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
24 18

출력) 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
6
72
 */
public class Main {

    public static void main(String args[]) throws IOException {
        
        int gcd = 0; // 최대공약수(GCD: Greatest Common Divisor)
        int lcm = 0; // 최소공배수(LCM: Least Common Multiple)

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        br.close();

        // 최대공약수, 최소공배수 구하기
        gcd = getGcd(a, b);
        lcm = getLcm(a, b, gcd);

        // 출력
        System.out.println(gcd);
        System.out.println(lcm);

        return;
    }

    // 최대공약수 구하기 (유클리드 호제법)
    private static int getGcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

    // 최대공배수 구하기
    private static int getLcm(int a, int b, int gcd) {
        return a * b / gcd;
    }
}