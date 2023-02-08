import cv2
from sudoku_reader import *
from sudoku_solver import *
from sudoku_valid import *


if __name__ == "__main__":

    img = "6.png"  # Imagen
    board = cv2.imread("test/" + img)  # Carga de imagen
    board, predictions = predict(board, find_board=True, show_boxes=False, show_board=False)  # Lectura de la imagen
    """
    find_board --> Encontrar recuadro del sudoku / Find board in the image
    show_boxes --> Mostrar todas las imágenes de los números del sudoku / Show all images of sudoku numbers
    show_board --> Mostrar sudoku entero / show entire sudoku
    """
    print(board)  # Mostrar sudoku leído
    print("#-------------x-------------#")
    solve_sudoku(board)  # Resolver sudoku
    print(board)  # Mostrar sudoku resuelto
    print(valid_sudoku(board))  # Valida si el sudoku está resuelto correctamente
