class Solution {
    fun solution(s: String): Boolean {
        var answer = true
        var arr = s.toCharArray()
        for(i in 'A'..'z'){
            if(s.contains(i)==true||(arr.size!=4&&arr.size!=6)){
                    answer=false
            }
        }
        return answer
    }
}