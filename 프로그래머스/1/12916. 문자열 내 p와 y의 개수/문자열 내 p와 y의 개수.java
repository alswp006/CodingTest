class Solution {
    boolean solution(String s) {
        int p = 0;
        int y = 0;
        s = s.toUpperCase();

        for (int i = 0; i< s.length(); i++){
            char temp = s.charAt(i);
            p += (temp=='P'?1:0);
            y += (temp=='Y'?1:0);
        }
        
        return p==y;
    }
}