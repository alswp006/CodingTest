class Solution {
    fun solution(n: Long): IntArray {
        var answer = ArrayList<Int>()
        var input:Long = n

        while(input!=0L){
            answer.add((input%10L).toInt())
            input/=10L
        }
        
        return answer.toIntArray()
    }
}