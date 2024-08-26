package Alogorithm.java;

public class 없는숫자더하기 {
    class Solution {
        public int solution(int[] numbers) {
            int answer = 0;
            int[] input = new int[10];
            for (int i = 0; i < numbers.length; i++) {
                input[numbers[i]] = 1;
            }
            for (int i = 0; i < input.length; i++) {
                if (input[i] == 0) {
                    answer += i;
                }
            }

            return answer;
        }
    }}
