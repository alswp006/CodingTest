class Solution {
    public long solution(long n) {
        return (n%Math.pow(n,0.5)==0?Math.round(Math.pow(Math.pow(n,0.5)+1, 2)):-1);
    }
}