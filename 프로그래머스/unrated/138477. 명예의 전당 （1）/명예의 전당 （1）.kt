class Solution {
    fun solution(k: Int, score: IntArray): IntArray {
        var answer: IntArray = IntArray(score.size)
        var list = mutableListOf(score[0],score[1],score[2])
        list.sort()
        answer[0] = score[0]
        if(score[0]>score[1]) answer[1] = score[1]
        else answer[1] = score[0]
        answer[2] = list[0]
        for(i in 3 until score.size){
            if(k>i){
                list.add(score[i])
                list.sort()
                answer[i] = list[0]
            }
            else{
                if(list[0]>=score[i]){
                    answer[i] = list[0]
                    continue
                }
                else{
                    list.remove(list[0])
                    list.add(score[i])
                    list.sort()
                    answer[i] = list[0]
                }
            }
        }
        return answer
    }
}