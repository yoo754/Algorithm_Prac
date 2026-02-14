import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        
        
        //commands[i][0] i만 바뀌고 [0] [1] [2]는 고정
        for(int c =0 ; c < commands.length; c++) {
            
            ArrayList<Integer> list = new ArrayList<>();
            int i = commands[c][0];
            int j = commands[c][1];
            int k = commands[c][2];


            for(int t = i; t<=j; t++) {
                list.add(array[t-1]);
            }
            // System.out.println(list);
            
            Collections.sort(list);
            answer[c] = list.get(k-1);
        }
        
        
            
        return answer;
    }
}