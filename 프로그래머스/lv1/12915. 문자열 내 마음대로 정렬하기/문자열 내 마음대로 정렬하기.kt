class Solution {
    fun solution(strings: Array<String>, n: Int): List<String> {
        return strings.sorted().sortedBy{it[n]}
    }
}