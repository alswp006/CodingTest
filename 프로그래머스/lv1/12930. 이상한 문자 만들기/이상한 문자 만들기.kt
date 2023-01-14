class Solution {
    fun solution(s: String): String {
        var answer : String = ""
        var arr = s.toCharArray()
        var count = 0
        for(i in 1 .. arr.size){
            if(arr[i-1]==' ') count = 1
            if(count%2==0) answer += arr[i-1].uppercaseChar()
            else answer += arr[i-1].lowercaseChar()
            count+=1
        }
        return answer
    }
}