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

## Contacto
[![image](https://camo.githubusercontent.com/c873e86c083c071c7fd068a17ab549b763fad7088681d6d831f68b32a4305b3a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f776562736974652d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d41626f75742e6d65266c6f676f436f6c6f723d7768697465)](https://julianprieto21.github.io/Portfolio-Website/)
[![image](https://camo.githubusercontent.com/a80d00f23720d0bc9f55481cfcd77ab79e141606829cf16ec43f8cacc7741e46/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d3030373742353f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/julian-prieto-809397253/)
[![image](https://camo.githubusercontent.com/571384769c09e0c66b45e39b5be70f68f552db3e2b2311bc2064f0d4a9f5983b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476d61696c2d4431343833363f7374796c653d666f722d7468652d6261646765266c6f676f3d676d61696c266c6f676f436f6c6f723d7768697465)](mailto:prietojulian2003@gmail.com)
