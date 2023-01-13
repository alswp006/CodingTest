class Solution {
    fun solution(a: Int, b: Int): Long {
        var answer: Long = 0
        var min:Long
        var max:Long
        var sum:Long = 0L
        if(a<b){
            min = a.toLong()
            max = b.toLong()
        }
        else{
            min = b.toLong()
            max = a.toLong()
        }
        for(i in min .. max){
            sum+=i
        }
        answer = sum.toLong()
        return answer
    }
}