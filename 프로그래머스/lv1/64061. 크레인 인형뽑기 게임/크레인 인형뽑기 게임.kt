class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        var basket = mutableListOf<Int>()
        var arr = board
        for(i in 0 until moves.size){
            for(j in 0 until board.size){
                if(arr[j][moves[i]-1]==0) continue
                else{
                    basket.add(arr[j][moves[i]-1])
                    arr[j][moves[i]-1]=0
                    if(basket.size>1){
                	    if(basket.last()==basket[basket.size-2]){
                  	        basket.removeLast()
                            basket.removeLast()
                    	    answer+=2
                  	    }
                    }
                    break
                }
            }
        }
        return answer
    }
}