import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        boolean[] visited = new boolean[n];
        
        
        for(int i = 0; i < n; i++) {
            if(visited[i]) continue;
            answer++;
            
            Deque<Integer> dq = new ArrayDeque<>();
            
            dq.offer(i);
            visited[i] =true;
            
            while(!dq.isEmpty()) {
                int now = dq.poll();
                
                for(int j = 0; j<n ; j++) {
                    if(computers[now][j] == 1 && !visited[j]) {
                        visited[j] = true;
                        dq.offer(j);
                    }
                    
                }
            }
        }
        return answer;
    }
}