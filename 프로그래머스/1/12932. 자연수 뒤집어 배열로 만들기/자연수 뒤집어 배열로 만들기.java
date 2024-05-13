import java.util.*;

class Solution {
    public int[] solution(long n) {
        List<Integer> arr = new ArrayList<Integer>();
        while (n>0){
            arr.add(Long.valueOf(n%10).intValue());
            n/=10;
        }
        
        int[] answer = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++){
            answer[i] = arr.get(i);
        }
        return answer;
    }
}