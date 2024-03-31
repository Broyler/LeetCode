# Time: O(1)
# Space: O(1) 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for x in range(9):
            for y in range(9):
                if board[y][x] == '.':
                    continue
                if (board[y][x] in rows[x] or
                    board[y][x] in cols[y] or
                    board[y][x] in boxes[(x // 3, y // 3)]):
                    return False
                rows[x].add(board[y][x])
                cols[y].add(board[y][x])
                boxes[(x // 3, y // 3)].add(board[y][x])
        return True
