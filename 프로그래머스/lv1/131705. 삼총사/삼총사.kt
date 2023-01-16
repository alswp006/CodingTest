class Solution {
    fun solution(number: IntArray): Int {
        var answer: Int = 0
        for(i in 0 until number.size){
            for(j in i+1 until number.size){
                for(k in j+1 until number.size){
                    if(number[i]+number[j]+number[k]==0) answer+=1
                }
            }
        }
        return answer
    }
}