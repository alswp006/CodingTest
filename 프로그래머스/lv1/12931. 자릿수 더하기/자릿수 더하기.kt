class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var a = n
        while(a!=0){
            answer += a%10
            a/=10
        }
        return answer
    }
}