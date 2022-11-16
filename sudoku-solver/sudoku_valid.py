

def valid_row(sudoku):
    for row in sudoku:
        numbers = []
        for number in row:
            if not number in numbers:
                numbers.append(number)
            else:
                return False
    return True


def valid_col(sudoku):
    for i in range(9):
        col = []
        for row in sudoku:
            col.append(row[i])
        numbers = []
        for number in col:
            if not number in numbers:
                numbers.append(number)
            else:
                return False
    return True


def valid_square(sudoku):
    for x in range(0,7,3):
        rows = sudoku[x:x+3]
        for y in range(0,7,3):
            box = []
            for i in range(3):
                for j in range(y,y+3):
                    box.append(rows[i][j])
            numbers = []
            for number in box:
                if not number in numbers:
                    numbers.append(number)
                else:
                    return False
    return True


def valid_sudoku(x):

    X = []
    sudoku = []
    for row in x:
        for i in row:
            X.append(i)
        sudoku.append(X)
        X = []

    valid = {
        "Filas" : valid_row(sudoku),
        "Columnas" : valid_col(sudoku),
        "Cajas" : valid_square(sudoku)
    }
    for key, bool in valid.items():
        if not bool:
            return f"Hay un error en las {key}"
    return "El sudoku esta bien resuelto!"

    