class Solution {
    fun solution(s: String): String {
        var answer = ""
        var leng = 0
        if(s.length%2==0){
            answer = s.substring(s.length/2-1 .. s.length/2)
        }
        else{
            answer = s.substring((s.length-1)/2..(s.length-1)/2)
        }
        return answer
    }
}