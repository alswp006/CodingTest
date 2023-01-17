import java.util.*

class Solution {
    fun solution(k: Int, m: Int, score: IntArray): Int {
        var answer: Int = 0
        score.sortDescending()
        var num =0
        score.forEach{
            num+=1
            if(num%m == 0){
               answer+= it*m
            }
        }
        return answer
    }
}