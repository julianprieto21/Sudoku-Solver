
def _find_next_empty(sudoku):
    """ 
    Encuentra el siguiente espacio que no este completado aun --> 0
    """
    #Devuelve (fila, columna) or (None, None) si no hay espacion vacios
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None

def _is_valid(sudoku, guess, row, col):
    """
    Verifica si la prediccion de un valor es valido en el tablero
    """
    # Se fija si guess en (fila, columna) es valido
    # Devuelte True si lo es, False si no lo es
    # primero las filas
    row_vals = sudoku[row]
    if guess in row_vals:
        return False

    # despues las columnas
    col_vals = [sudoku[i][col] for i in range(9)]
    if guess in col_vals:
        return False 
    
    # y luego la box (3x3)
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if sudoku[i][j] == guess:
                return False

    # Si llega hasta aca es que es valido = True
    return True

def solve_sudoku(sudoku):
    """
    Resuelve el sudoku utilizando otras funciones
    """
    # Resuelve el sudoku
    row, col = _find_next_empty(sudoku)
    
    if row is None:
        return True
    
    for guess in range(1, 10):
        if _is_valid(sudoku, guess, row, col):
            # Colocar guess en el sudoku
            sudoku[row][col] = guess

            if solve_sudoku(sudoku):
                return True
            
        # si no es valido, o no resuelve el sudoku, volvemos atras y
        # probamos otro numero
        sudoku[row][col] = 0 # Resetea el numero
    
    return False
