from image_reader import ImageReader
from sudoku import Sudoku


if __name__ == "__main__":
    reader = ImageReader("test/4.png")
    sudoku_board = reader.get_sudoku()
    sudoku = Sudoku(sudoku_board)
    sudoku.solve()
    sudoku.valid_solution()
