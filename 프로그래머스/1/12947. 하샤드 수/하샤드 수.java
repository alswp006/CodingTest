class Solution {
    public boolean solution(int x) {
        int temp = x;
        int hashard = 0;
        
        while (temp > 0){
            hashard += temp % 10;
            temp /= 10;
        }
        
        return x % hashard == 0;
    }
}