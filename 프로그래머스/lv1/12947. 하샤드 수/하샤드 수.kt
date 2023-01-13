class Solution {
    fun solution(x: Int): Boolean {
        var answer = true
        var sum = 0
        var input = x
        while(input!=0){
            sum+=input%10
            input/=10
        }
        if(x%sum==0){
            answer = true
        }
        else{
            answer = false
        }
        return answer
    }
}