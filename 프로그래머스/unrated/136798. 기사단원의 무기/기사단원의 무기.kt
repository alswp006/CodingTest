import kotlin.math.sqrt

class Solution {
    fun numbers(num : Int,limit :Int,power: Int) : Int{
        var count = 0 
        var nums = sqrt(num.toDouble()).toInt()
        for(i in 1 .. nums){
            if(i*i==num) count+=1
            else if(num%i==0) {
                count+=2
            }
            if(count>limit) {
                count = power
                break
            }
            
        }
        return count
    }
    fun solution(number: Int, limit: Int, power: Int): Int {
        var answer: Int = 0
        for(i in 0 until number){
            var n = numbers(i+1,limit,power)
            answer+=n
        }
        return answer
    }
}