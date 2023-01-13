class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer = intArrayOf()
        var arr1 = arr.toList()
        var a = arr1.minOrNull()
        if(arr.size!=1) answer = arr.filter{it!=a}.toIntArray()
        else answer = intArrayOf(-1)
        return answer
    }
}