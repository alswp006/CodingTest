class Solution {
    fun solution(answers: IntArray): IntArray {
        var n1 = mutableListOf(1,2,3,4,5)
        var first = mutableListOf<Int>()
        var n2 = mutableListOf(2,1,2,3,2,4,2,5)
        var second = mutableListOf<Int>()
        var n3 = mutableListOf(3,3,1,1,2,2,4,4,5,5)
        var third = mutableListOf<Int>()
        var c1 = 0
        var c2 = 0
        var c3 = 0
        for(i in 0 until answers.size){
            first.add(n1.first())
            n1.add(n1.first())
            n1.remove(n1.first())
            second.add(n2.first())
            n2.add(n2.first())
            n2.remove(n2.first())
            third.add(n3.first())
            n3.add(n3.first())
            n3.remove(n3.first())
        }
        for(i in 0 until answers.size){
            if(answers[i]==first[i]) c1+=1
            if(answers[i]==second[i]) c2+=1
            if(answers[i]==third[i]) c3+=1
        }
        var answer = mutableListOf<Int>()
        if(c1==c2&&c2==c3) {
            answer.add(1)
            answer.add(2)
            answer.add(3)
        }
        else if(c1==c2&&c2>c3) {
            answer.add(1)
            answer.add(2)
        }
        else if(c2==c3&&c2>c1) {
            answer.add(2)
            answer.add(3)
        }
        else if(c1==c3&&c3>c2) {
            answer.add(1)
            answer.add(3)
        }
        else if(c1>c3&&c2<c1) {answer.add(1)}
        else if(c1<c2&&c3<c2) {answer.add(2)}
        else if(c1<c3&&c2<c3) {answer.add(3)}
        
        return answer.toIntArray()
    }
}