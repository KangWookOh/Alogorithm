package Alogorithm.java;

public class 나머지가1이되는숫자찾기 {
    class Solution {
        public int solution(int n) {
            int answer = 0;
            for(int i=2; i<n; i++){

                if(n%i==1){
                    answer =i;
                    break;
                }
            }
            return answer;
        }
    }
}
