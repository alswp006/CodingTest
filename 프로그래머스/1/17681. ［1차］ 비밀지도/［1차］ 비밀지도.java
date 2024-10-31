class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++){
            String s1 = String.format("%16s", Integer.toBinaryString(arr1[i])).replace(" ","0").substring(16 - n);
            String s2 = String.format("%16s", Integer.toBinaryString(arr2[i])).replace(" ","0").substring(16-n);
            StringBuilder sb = new StringBuilder();
            
            for (int j = 0; j < n; j++){
                if (s1.charAt(j) == '1' || s2.charAt(j) == '1') sb.append("#");
                else sb.append(" ");
            }
            answer[i] = sb.toString();
            
        }
        return answer;
    }
}