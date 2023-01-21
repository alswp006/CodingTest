class Solution {
    fun solution(s: String): String {
        var arr = s.split(" ").toTypedArray()
        for(i in 0 until arr.size){
            arr[i] = arr[i].lowercase().capitalize()    
        }
        return arr.joinToString(" ")
    }
}