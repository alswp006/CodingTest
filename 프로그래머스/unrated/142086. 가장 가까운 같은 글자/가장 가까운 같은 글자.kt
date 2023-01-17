class Solution {
    fun solution(s: String): IntArray {
        var answer: IntArray = IntArray(s.length)
        answer[0] = -1
        for(i in 1 until s.length){
            for(j in i-1 downTo(0)){
                if(s[i]==s[j]){
                    answer[i]=i-j
                    break
                }
                else answer[i] = -1
            }
        }
        return answer
    }
}