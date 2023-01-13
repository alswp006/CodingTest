class Solution {
    fun solution(x: Int, n: Int): LongArray {
        var answer = LongArray(n)
        var a = x.toLong()
        for(i in 0 until n){
            answer[i] = a + i * a
        }
        return answer
    }
}