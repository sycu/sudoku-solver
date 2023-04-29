from sudoku import Grid


class Rule:
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        pass


class SudokuRow(Rule):
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        for i in range(9):
            if sudoku[y][i] == value:
                return False

        return True


class SudokuColumn(Rule):
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        for i in range(9):
            if sudoku[i][x] == value:
                return False

        return True


class SudokuSquare(Rule):
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for j in range(y0, y0 + 3):
            for i in range(x0, x0 + 3):
                if sudoku[j][i] == value:
                    return False

        return True


class KnightMove(Rule):
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        positions = [
            (x - 1, y + 2),
            (x + 1, y + 2),
            (x - 1, y - 2),
            (x + 1, y - 2),
            (x - 2, y + 1),
            (x + 2, y + 1),
            (x - 2, y - 1),
            (x + 2, y - 1),
        ]

        for x0, y0 in positions:
            if 0 <= x0 < 9 and 0 <= y0 < 9 and sudoku[y0][x0] == value:
                return False

        return True


class KingMove(Rule):
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        positions = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]

        for x0, y0 in positions:
            if 0 <= x0 < 9 and 0 <= y0 < 9 and sudoku[y0][x0] == value:
                return False

        return True


class OrthagonallyAdjacentNotConsecutive(Rule):
    def is_valid_move(self, sudoku: Grid, x: int, y: int, value: int) -> bool:
        positions = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        for x0, y0 in positions:
            if 0 <= x0 < 9 and 0 <= y0 < 9 and 1 <= sudoku[y0][x0] <= 9 and abs(sudoku[y0][x0] - value) < 2:
                return False

        return True