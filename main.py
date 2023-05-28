from image_reader import ImageReader
from sudoku import Sudoku
"""
Versiones necesarias:
Tensorflow 2.11.0
Keras 2.11.0
"""


if __name__ == "__main__":
    reader = ImageReader("test/2.png")
    sudoku_board = reader.get_sudoku()
    sudoku = Sudoku(sudoku_board)
    sudoku.solve()
    sudoku.valid_solution()
