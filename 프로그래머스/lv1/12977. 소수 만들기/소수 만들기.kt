class Solution {
    fun solution(nums: IntArray): Int {
        var answer = 0
        var count = 0
        var sum = 0
        for(i in 0 until nums.size-2){
            for(j in i+1 until nums.size-1){
                for(k in j+1 until nums.size){
                    sum = nums[i]+nums[j]+nums[k]
                    for(a in 2..sum){
                        if(sum%a==0) {
                            count+=1
                        }
                    }
                    if(count==1) answer+=1
                    sum = 0
                    count = 0
                }
            }
        }
        return answer
    }
}