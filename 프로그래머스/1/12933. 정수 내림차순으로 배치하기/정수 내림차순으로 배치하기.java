import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        List<Integer> arr = new ArrayList<Integer>();
        
        while (n > 0){
            arr.add(Long.valueOf(n%10).intValue());
            n/=10;
        }
        
        Collections.sort(arr);
        int temp = 1;
        for (int i : arr){
            answer += Long.valueOf(i) * temp;
            temp *= 10;
        }
        return answer;
    }
}