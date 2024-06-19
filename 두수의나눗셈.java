package Alogorithm;

public class 두수의나눗셈 {
    class Solution {
        public int solution(int num1, int num2) {
            double answer = 0;
            answer = (double)num1 /num2;
            answer = answer * 1000;

            return (int)answer;
        }
    }
}
