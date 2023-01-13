import kotlin.math.*

class Solution {
    fun solution(n: Long): Long {
        var answer: Long = 0
        var a = sqrt(n.toDouble())
        if(a%1==0.0){
            answer = (a+1).pow(2).toLong()
        }
        else{
            answer = -1
        }
        return answer
    }
}