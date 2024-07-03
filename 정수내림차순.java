package Alogorithm;
import java.util.*;

public class 정수내림차순 {

    class Solution {
        public long solution(long n) {
            long answer = 0;
            String[] arr = String.valueOf(n).split("");
            Arrays.sort(arr);

            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < arr.length; i++) {
                sb.append(arr[i]); // 문자 하나씩 합치기
            }

            return Long.parseLong(sb.reverse().toString());
        }
    }
}
