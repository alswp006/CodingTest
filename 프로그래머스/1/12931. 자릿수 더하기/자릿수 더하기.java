import java.util.*;
import java.util.stream.IntStream;

public class Solution {
    public int solution(int n) {
        return IntStream.of(Integer.toString(n).chars().map(c -> c-'0').toArray()).sum();
    }
}