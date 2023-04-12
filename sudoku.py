import copy


class Sudoku:
    """
    Clase que representa un tablero de sudoku
    """
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.solution = copy.deepcopy(sudoku)
        self.solved = False
        self.count = 0

    def _find_next_empty(self):
        """
        Encuentra el siguiente espacio que no esté completado aun --> 0
        :return: (fila, columna) or (None, None) si no hay espacios vacíos
        """
        next_empty = [(i, j) for i in range(9) for j in range(9) if self.solution[i][j] == 0]
        if len(next_empty) == 0:
            return None, None
        return next_empty[0]

    def _is_valid(self, guess, r, c):
        """
        Verifica si la predicción de un valor es válido en el tablero
        :param guess: predicción
        :param r: fila de la predicción
        :param c: columna de la predicción
        :return: True si es válido, False si no lo es
        """
        # Verifica si guess en (fila, columna) es válido
        row = self.solution[r]
        if guess in row:
            return False
        col = [self.solution[i][c] for i in range(9)]
        if guess in col:
            return False
        # Verifica la caja (3x3)
        row_start = (r // 3) * 3
        col_start = (c // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.solution[i][j] == guess:
                    return False
        # En este punto guess es válido
        return True

    def solve(self):
        """
        Resuelve el sudoku
        :return: Sudoku resuelto
        """
        self.count += 1
        r, c = self._find_next_empty()
        # Si no hay espacios vacíos, el sudoku está resuelto
        if r is None:
            return True
        # Si hay espacios vacíos, prueba con los números del 1 al 9
        for guess in range(1, 10):
            if self._is_valid(guess, r, c):
                # Si es válido, coloca el número en el espacio vacío
                self.solution[r][c] = guess
                # Llama a la función recursivamente
                if self.solve():
                    if not self.solved:
                        # Si el sudoku está resuelto, imprime el sudoku inicial y el resuelto
                        self.solved = True
                        print("Sudoku inicial: ")
                        self.print(self.sudoku)
                        print(" ")
                        print("Sudoku resuelto: ")
                        self.print(self.solution)
                        print("Iteraciones: ", self.count)
                    return True
                # Si no es válido, vuelve a 0
                self.solution[r][c] = 0
        # Si no hay números válidos, devuelve False
        return False

    @classmethod
    def print(self, sudoku):
        """
        Imprime el sudoku
        :param sudoku: Sudoku a imprimir
        :return: Sudoku impreso
        """
        for i in range(len(sudoku)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(len(sudoku[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    if sudoku[i][j] == 0:
                        print("_")
                    else:
                        print(sudoku[i][j])
                else:
                    if sudoku[i][j] == 0:
                        print("_ ", end="")
                    else:
                        print(str(sudoku[i][j]) + " ", end="")

    def get_sudoku(self):
        """
        Devuelve el sudoku inicial
        :return: Sudoku inicial
        """
        self.print(self.sudoku)

    def get_solution(self):
        """
        Devuelve la solución del sudoku
        :return: Sudoku resuelto
        """
        self.print(self.solution)

    def valid_solution(self):
        """
        Verifica si la solución del sudoku es válida
        :return: True si es válida, False si no lo es
        """
        # Validar filas
        for i in range(9):
            fila = self.solution[i,:]
            if len(set(fila)) != 9 or 0 in fila:
                print("Solución inválida: Fila")
                return False
        
         # Validar columnas
        for j in range(9):
            columna = self.solution[:,j]
            if len(set(columna)) != 9 or 0 in columna:
                print("Solución inválida: Columna")
                return False
        
        # Validar subcuadros
        for k in range(3):
            for l in range(3):
                subcuadro = self.solution[k*3:k*3+3,l*3:l*3+3].flatten()
                if len(set(subcuadro)) != 9 or 0 in subcuadro:
                    print("Solución inválida: Subcuadro")
                    return False
        
        # Si todos los valores son únicos y diferentes de cero, entonces es una solución válida
        print("Solución válida")
        return True
