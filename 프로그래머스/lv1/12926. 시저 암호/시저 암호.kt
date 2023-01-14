class Solution {
    fun solution(s: String, n: Int): String {
        var arr = s.toCharArray()
        var answer = ""
        for(i in 0 until arr.size){
            if(arr[i]==' '){ 
                answer += ' '
                continue
            }
            if('a'<=arr[i]&&arr[i]<='z'){
                if((arr[i]+n)>'z') answer += 'a'+(n-1-'z'.toInt()+arr[i].toInt())
                else answer += arr[i]+n
            }
            else{
                if((arr[i]+n)>'Z') answer += 'A'+(n-1-'Z'.toInt()+arr[i].toInt())
                else answer += arr[i]+n
            }
        }

        return answer
    }
}