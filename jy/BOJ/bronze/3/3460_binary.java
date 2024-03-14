import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 3460. 이진수
public class Main {
    public static void main(String args[]) throws IOException {
        
        int T = 0; // 테스트케이스 개수

        // @ 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        T = Integer.parseInt(new StringTokenizer(tmp).nextToken().trim());
        
        for (int i=0; i<T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            // 양의 정수 n을 이진수로 나타냈을 때 1의 위치 출력
            locationOfOne(n);
        }
        
        br.close();
        
        return;
    }

    // 양의 정수 n을 이진수로 나타냈을 때 1의 위치 출력
    private static void locationOfOne(int n) {
        StringBuffer sb = new StringBuffer();

        // 이진수 변환
        String nString = Integer.toBinaryString(n);

        // 1의 위치 찾기
        for (int i=0; i<nString.length(); i++) {
            if (nString.charAt(i) == '1') {
                sb.insert(0, (nString.length()-i-1));
                sb.insert(0, ' ');
            }
        }
        sb.deleteCharAt(0);

        // 출력
        System.out.println(sb);
    }
}