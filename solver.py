from numpy import array
from rules import Rule, SudokuColumn, SudokuRow, SudokuSquare, KnightMove, KingMove, OrthogonallyAdjacentNotConsecutive, OrthogonallyAdjacentHaveCommonDivisor
from sudoku import Grid
from typing import Generator, List


class SudokuSolver:
    def solve(self, rules: List[Rule], sudoku: Grid) -> Generator[Grid, None, None]:
        for y in range(9):
            for x in range(9):
                if not sudoku[y][x]:
                    for value in range(1, 10):
                        if self.__is_valid_move(rules, sudoku, x, y, value):
                            sudoku[y][x] = value
                            yield from self.solve(rules, sudoku)
                            sudoku[y][x] = 0

                    return None

        yield sudoku

    def __is_valid_move(self, rules: List[Rule], sudoku: Grid, x: int, y: int, value: int) -> bool:
        for rule in rules:
            if not rule.is_valid_move(sudoku, x, y, value):
                return False

        return True


if __name__ == '__main__':
    hard = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
    ]

    easy_single = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    easy_multiple = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    empty = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    test = [
        [0, 0, 8, 0, 0, 0, 2, 4, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 3, 8],
        [1, 0, 0, 5, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 3],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
    ]

    rules = [
        SudokuColumn(),
        SudokuRow(),
        SudokuSquare(),
        # KnightMove(),
        # KingMove(),
        # OrthogonallyAdjacentNotConsecutive(),
        OrthogonallyAdjacentHaveCommonDivisor(),
    ]
    solver = SudokuSolver()
    for solution in solver.solve(rules, test):
        print(array(solution))
