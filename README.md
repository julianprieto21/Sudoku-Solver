# Sudoku-Solver
Program in Python to solve sudoku puzzles from images, using TensorFlow (Keras) and Backtracking Algorithms.

![sudoku](https://user-images.githubusercontent.com/114876710/227323107-eed94efb-6064-4e63-82fa-ba9311e46b9a.jpg)

Este proyecto se me ocurrio en un momento donde buscaba alguna manera de ejercer los conocimientos que fui adquiriendo en Python y en el Machine Learning.

Fue mi primer real proyecto en este lenguaje y me presentó varios desafios relacionados con el modelo, con la logica, con el algoritmo de resolucion, etc.
Aún sigue en desarrollo (pausado) ya que presenta algunos problemas al detectar correctamente los numeros de la imagen pasada. Sin embargo, resuelve correctamente cualquier sudoku en cuestion de segundos.
## Aclaraciones:
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

# Sudokus de prueba extraidos de
https://www.rd.com/list/printable-sudoku-puzzles/
