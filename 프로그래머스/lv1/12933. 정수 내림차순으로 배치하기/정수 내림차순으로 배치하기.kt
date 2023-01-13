class Solution {
    fun solution(n: Long): Long {
        var answer: Long = String(n.toString().toCharArray().sortedArrayDescending()).toLong()
        return answer
    }
}