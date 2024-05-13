import java.util.*;

class Solution {
    public int[] solution(long n) {
                return new StringBuilder().append(n).reverse().chars().map(c -> c - '0').toArray();

    }
}