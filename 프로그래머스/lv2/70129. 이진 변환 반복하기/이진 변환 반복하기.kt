class Solution {
    fun solution(s: String): IntArray {
        var answer: IntArray = IntArray(2){0}
        var c = s
        while(c!="1"){
            answer[1] += c.filter{it=='0'}.count()
            c = c.replace("0","")
            c=c.length.toString(2)
            answer[0]++
        }
        return answer
    }
}