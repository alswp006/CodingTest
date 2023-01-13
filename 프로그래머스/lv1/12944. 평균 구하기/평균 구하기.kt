class Solution {
    fun solution(arr: IntArray): Double {
        var answer: Double
        var sum : Double = 0.0
        
        for(i in 0 until arr.size){
            sum+=arr[i]
        }
        answer = sum / arr.size
        
        return answer
    }
}