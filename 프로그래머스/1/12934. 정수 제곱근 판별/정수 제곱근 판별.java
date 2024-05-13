class Solution {
    public long solution(long n) {
        return (n%Math.sqrt(n)==0?Math.round(Math.pow(Math.sqrt(n)+1, 2)):-1);
    }
}