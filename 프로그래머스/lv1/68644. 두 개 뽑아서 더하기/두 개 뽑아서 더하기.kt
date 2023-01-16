class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = ArrayList<Int>()
        var a = 0
        for(i in 0 until numbers.size){
            for(j in  0 until numbers.size){
                if(i!=j){ a = numbers[i] + numbers[j]
                if(answer.indexOf(a)==-1) answer.add(a)}
            }
        }
        return answer.toIntArray().sortedArray()
    }
}