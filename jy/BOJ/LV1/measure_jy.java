import java.util.*;

public class Main {
    public static void main(String args[]) {

      // @ 입력 받기
      Scanner sc = new Scanner(System.in);
      String str = sc.nextLine();
      sc.close();
      
      String[] tempStr = str.split(" ");
      int N = Integer.parseInt(tempStr[0]);
      int K = Integer.parseInt(tempStr[1]);
      int returnValue = 0;

      // @ N의 약수 구하기
      ArrayList<Integer> list = new ArrayList<Integer>();
      for (int i=1; i<=Math.sqrt(N); i++) {
          int temp = N % i;
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
          returnValue = list.get(K - 1);
      }
      
      
      System.out.println(returnValue);

      return;
    }
}