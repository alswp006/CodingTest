class Solution {
    fun solution(n: Int): String {
        var answer = ""
        for(i in 1..n/2+1){
            answer = answer.plus("수박")
        }
        if(n%2!=0){
            answer = answer.substring(0 until answer.length-1)
        }
        else{
            answer = answer.substring(0 until answer.length-2)
        }
        return answer
    }
}