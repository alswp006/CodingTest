class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        var answer = ArrayList<Int>()
        for(i in 0 until arr.size){
            if(arr[i]%divisor==0){
                answer.add(arr[i])
            }
        }
        return if(answer.size==0) intArrayOf(-1) else answer.toIntArray().sortedArray()
    }
}