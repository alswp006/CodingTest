class Solution {
    public int solution(int[][] sizes) {
        int max_v = 0;
        int max_h = 0;
            
        for (int[] i : sizes){
            max_v = Math.max(Math.max(i[0], i[1]), max_v);
            max_h = Math.max(Math.min(i[0], i[1]), max_h);
        }

        return max_v * max_h;
    }
}