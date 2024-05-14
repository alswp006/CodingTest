import java.util.*;


class Solution {
    public double solution(int[] arr) {
        return Double.valueOf(Arrays.stream(arr).sum())/Double.valueOf(arr.length);
    }
}