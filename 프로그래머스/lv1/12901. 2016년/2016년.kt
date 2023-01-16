class Solution {
    fun solution(a: Int, b: Int): String {
        val Week = listOf("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")
        val year = listOf(31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        var xDay = (0 until a - 1).map {
            year[it]
        }.sum() + b
        return Week[xDay%7]
    }
}