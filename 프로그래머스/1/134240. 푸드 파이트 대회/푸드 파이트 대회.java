class Solution {
    public String solution(int[] food) {
        StringBuilder answer = new StringBuilder();
        
        for (int i = 1; i < food.length; i++){
            for (int j = 0; j < food[i] / 2; j++){
                answer.append(String.valueOf(i));
            }    
        }
        return answer.toString() + "0" + answer.reverse().toString();
    }
}