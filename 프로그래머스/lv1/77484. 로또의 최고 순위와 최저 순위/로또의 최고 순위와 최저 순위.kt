class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var zero = lottos.count{it==0}
        var count = 0
        for(i in 0 until lottos.size){
            count += lottos.count{it==win_nums[i]}
        }
        var max = 0
        var min = 0
        when(count){
            6 -> min=1
            5 -> min=2
            4 -> min=3
            3 -> min=4
            2 -> min=5
            else -> min=6
        }
        max=min-zero
        if(max<1) max=1
        answer = answer.plus(max)
        answer = answer.plus(min)
        return answer
    }
} //최저 순위 = 그냥 0인 상태에서 일치하는 숫자 갯수만
  //최고 순위 = 0 두개가 일치한다고 하면 최고 순위