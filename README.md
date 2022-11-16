# Sudoku-Solver
Program in Python to solve sudoku puzzles from images, using TensorFlow (Keras) and Backtracking Algorithms.

Aclaraciones:

En varios casos el modelo de lectura de numeros falla al reconocer correctamente
 y se suele confundir por ejemplo al 7 por un 1 o al 8 por un 0.

Esto provoca que el sudoku no pueda ser resuelto de manera correcta. Aunque
 hay casos donde aun asi (habiendolo leido mal) el programa logra encontrar una
 solucion

Para prevenir esto, se recomienda usar imagenes de alta calidad, lo que mejora
 la eficacia del modelo. Las imagenes usadas tienen una calidad superior a la
 de 1000x1000 pixeles.

En un futuro se mejorará el modelo detector de numeros con la intencion de que
 su eficacion aumente y no haya errores en la lectura.

# Dataset numeros extraido de 
https://www.kaggle.com/datasets/nimishmagre/tmnist-typeface-mnist?select=TMNIST_Data.csv

# Modelo extraido de 
https://www.kaggle.com/code/huchunjun/99-1-tmnist-typefacemnist-chunjunhu

# Sudokus extraidos de
https://www.rd.com/list/printable-sudoku-puzzles/
