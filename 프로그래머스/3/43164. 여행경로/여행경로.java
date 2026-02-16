import java.util.*;

class Solution {
    
    boolean[] visited;
    List<String> answer; 
    
    public String[] solution(String[][] tickets) {
        
        visited = new boolean[tickets.length];
        answer = new ArrayList<>();
            
        
        dfs("ICN", "ICN", tickets, 0);
        
        // route들어온거 처리해야됨
        
        Collections.sort(answer);
        
        return answer.get(0).split(",");
    }
    
    void dfs(String start, String route, String[][] tickets, int cnt) {
        
        // 탈출은 cnt == tickets.length 일 때
        
        if(cnt == tickets.length) {
            answer.add(route);
        }
        
        // 일단 시작지가 들어온 tickets[i][0]에서 위치를 찾아야함
        for(int i=0; i<tickets.length;i++) {
            if (tickets[i][0].equals(start) && !visited[i]) {
                // 찾으면 해당 tickets[i][1]에 박혀있는 값이 tickets[i][1]에 어딨는지 찾기
                visited[i] = true;
                
                dfs(tickets[i][1], route+ ","+tickets[i][1], tickets, cnt+1);
                
                visited[i]= false;
            }
        }
        
        
        
        
        
    }
}