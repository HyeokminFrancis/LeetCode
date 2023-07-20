class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_len = len(board[0])
        col_len = len(board)
        
        visited = [[0 for j in range(row_len)] for i in range(col_len)]
        
        def traverse(x, y, board: List[List[str]]):
            if(x < 0 or x > row_len-1 or y < 0 or y > col_len-1):
                return
            if(visited[y][x] == 1):
                return
            if(board[y][x] == 'X'):
                return
            
            visited[y][x] = 1
            
            traverse(x-1,y,board)
            traverse(x+1,y,board)
            traverse(x,y-1,board)
            traverse(x,y+1,board)
            
        for y in range(col_len):
            for x in range(row_len):
                if(y==0 or y==col_len-1 or x==0 or x==row_len-1):
                    traverse(x, y, board)
                    
        for y in range(col_len):
            for x in range(row_len):
                if(visited[y][x]==1):
                    continue
                board[y][x]='X'