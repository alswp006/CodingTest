class Solution {
    fun solution(left: Int, right: Int): Int {
        var answer: Int = 0
        var num =0
        for(i in left .. right){
            for(j in 1..i){
                if(i%j==0){
                    num +=1
                }
            }
            if(num%2==0){
                answer += i
            }
            else{
                answer -= i
            }
            num = 0
        }
        return answer
    }
}