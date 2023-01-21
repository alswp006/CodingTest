class Solution {
    fun solution(s: String): String {
        var answer = ""
        var arr1 = s.split(" ")
        var arr2 = IntArray(arr1.size)
        arr1.indices.forEach { arr2[it] = arr1[it].toInt() }
        arr2 = arr2.sortedArray()
        answer = answer.plus(arr2[0])
        answer = answer + " "
        answer = answer.plus(arr2[arr2.size-1])
        return answer
    }
}