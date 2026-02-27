import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
    
        int[][] rectangle2 = new int[rectangle.length][rectangle[0].length];
        
        // 좌표 2배 
        for(int i =0; i<rectangle.length ; i++){
            for(int j=0; j<rectangle[0].length; j++) {
                rectangle2[i][j] = 2*(rectangle[i][j]);
            }
        }
        
        //rectangle2 배열에서 가장 큰 값 뽑아내서 2배 시켜야함
        int max = 0;
        
        for(int i =0; i<rectangle2.length ; i++){
            for(int j=0; j<rectangle2[0].length; j++) {
                if(max < rectangle2[i][j]) {
                    max = rectangle2[i][j];
                }
            }
        }    

        
        int[][] maps = new int[max+2][max+2];
        // System.out.println(rectangle2[0][3]);
        
        //사각형 마다 전체 1 만들고 내부만 0으로 만들기
        for(int k = 0; k<rectangle2.length; k ++) { // 한바퀴 돌때마다 사각형 하나씩 채움
            int x1 = rectangle2[k][0]; // x1 2
            int y1 = rectangle2[k][1]; // y1 2
            int x2 = rectangle2[k][2]; // x2 14 
            int y2 = rectangle2[k][3]; // x2 8
            
            // System.out.println(x2);
            // 일단 사각형 전체 채움
            for (int x = x1; x <= x2; x++) {
                for (int y = y1; y<= y2; y++) {
                    maps[x][y] = 1;
                }
             }

        }
        
        for(int k = 0; k<rectangle2.length; k ++) { 
            int x1 = rectangle2[k][0]; 
            int y1 = rectangle2[k][1]; 
            int x2 = rectangle2[k][2]; 
            int y2 = rectangle2[k][3]; 
        
            // 사각형 내부 비움
            for (int xx = x1+1; xx < x2; xx++) {
                for (int yy = y1+1; yy< y2; yy++) {
                    maps[xx][yy] = 0;
                }
             }
        }

        // System.out.println(Arrays.deepToString(maps));
        
        boolean[][] visited = new boolean[max+2][max+2];
        Deque<int[]> dq = new ArrayDeque<>();
        
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        
        int[] start = {2*characterX, 2*characterY, 0}; 
        int[] end = {2*itemX, 2*itemY};
        
        dq.add(start);
        visited[2*characterX][2*characterY] = true;
        
        while(!dq.isEmpty()) {
            int[] now = dq.poll();
            int r = now[0];
            int c = now[1];
            int dist = now[2];
            
            if(r == end[0] && c == end[1]) {
                return dist/2;
            }
            
            for(int d = 0; d<4; d++) {
                int nr = dr[d] + r;
                int nc = dc[d] + c;
                
                if(0<=nr && nr< max+2 && 0 <= nc && nc < max+2 && maps[nr][nc] == 1 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    int[] next = {nr, nc, dist+1};
                    dq.add(next);
                }
            }
        }
        
        return 0;
    }
}