class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True
        
        def valid_column(board):
            for column in zip(*board):
                if not is_valid(column):
                    return False
            return True
        
        def valid_square(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3)
                                            for y in range(j, j + 3)]
                    if not is_valid(square):
                        return False
            return True
        
        def is_valid(numbers):
            res = [i for i in numbers if i != '.']
            return len(res) == len(set(res))
        
        return valid_row(board) and valid_column(board) and valid_square(board)
            
        