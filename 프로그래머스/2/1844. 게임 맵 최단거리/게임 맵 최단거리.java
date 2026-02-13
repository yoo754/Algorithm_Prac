import java.util.*;

class Solution {
    public int solution(int[][] maps) {        
        int N = maps.length;
        int M = maps[0].length;
        
        //bfs
        
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        
        // Set<String> visited = new HashSet<>(); // visited set
        boolean[][] visited = new boolean[N][M];
        Queue<int[]> queue = new LinkedList<>(); // queue
        
        queue.add(new int[]{0,0,1});
        visited[0][0] = true;
        
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            int r = now[0];
            int c = now[1];
            int dist = now[2];
            
            if(r == (N-1) && c == (M-1)) {
                return dist;
            }
            
            
            for(int d=0; d<4; d++) {
                int nr = dr[d] + r;
                int nc = dc[d] + c;
                
                if(0<=nr && nr<N &&
                  0<=nc && nc<M &&
                  maps[nr][nc] == 1 &&
                  !visited[nr][nc]) {
                    
                    visited[nr][nc] = true;
                    queue.add(new int[]{nr, nc, dist+1});

                }
                
            }
        }
        
        return -1;
    }
}