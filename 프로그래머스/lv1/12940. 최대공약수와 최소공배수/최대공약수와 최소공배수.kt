class Solution {
    fun solution(n: Int, m: Int): IntArray {
        var a = if(n<m) n else m
        var b = if(n<m) m else n
        var c = 0
        var d = 0
        for(i in 1..b){
            if(b%i==0&&a%i==0){
                c=i
            }
        }
        for(i in a..a*b){
            if(i%a==0&&i%b==0){
                d=i
                break
            }
        }
        var answer = intArrayOf(c,d)
        return answer
    }
}