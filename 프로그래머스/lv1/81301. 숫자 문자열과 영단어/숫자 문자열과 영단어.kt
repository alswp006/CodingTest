class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        var c :String = s
        var arr = arrayOf("zero","one","two","three","four","five","six","seven","eight","nine")
        for(i in 0 until 10){
            c = c.replace(arr[i],i.toString())
        }
        answer = c.toInt()
        return answer
    }
}