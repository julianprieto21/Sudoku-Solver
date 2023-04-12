import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
from number_model import NumberModel


class ImageReader:
    """
    Clase que lee una imagen y la prepara para ser procesada y leida
    """
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.modified_image = None
        self.numbers = []
        self.prediction = None
        self.model_engine = NumberModel(dt_path="TMNIST_Data.csv")

    def _init_image(self):
        """
        Lee la imagen y la guarda en self.image
        """
        self.image = cv2.imread(self.image_path)
        self.modified_image = cv2.imread(self.image_path)

    @staticmethod
    def show_image(image):
        """
        Muestra la imagen
        """
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def _alter_image(self):
        """
        Cambia la imagen para que sea más fácil de leer
        """
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.threshold(self.image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        self.modified_image = cv2.cvtColor(self.modified_image, cv2.COLOR_BGR2GRAY)
        self.modified_image = cv2.threshold(self.modified_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        self.modified_image = cv2.GaussianBlur(self.modified_image, (5, 5), 0)
        self.modified_image = cv2.morphologyEx(self.modified_image, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    
    def _find_contours(self):
        """
        Encuentra los contornos de la imagen
        """
        contours, hierarchy = cv2.findContours(self.modified_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        biggest_contour = max(contours, key=cv2.contourArea)
        return cv2.boundingRect(biggest_contour)

    def _crop_image(self):
        """
        Recorta la imagen para que solo quede el tablero
        """
        x, y, w, h = self._find_contours()
        self.image = self.image[y:y+h, x:x+w]
        self.modified_image = self.modified_image[y:y+h, x:x+w]

    def _prepare_image(self):
        """
        Prepara la imagen para ser procesada
        """
        self._init_image()
        self._alter_image()
        self._crop_image()
        self.image = cv2.resize(self.image, (900, 900))
        self.modified_image = cv2.resize(self.modified_image, (900, 900))

    def _split_numbers(self):
        """
        Separa los números del tablero. Los coloca dentro de self.numbers
        """
        contours, hierarchy = cv2.findContours(self.modified_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if (w == 90 and h == 90) or (w == 94 and h == 90) or (w == 90 and h == 94) or (w == 94 and h == 94):
                self.numbers.append(self.image[y:y+h, x:x+w])

    def _predict_numbers(self, model):
        """
        Predice los números del tablero
        """
        predictions = []
        for num in self.numbers:
            num = cv2.resize(num, (28, 28)) / 255
            num = num.reshape(1, 28, 28, 1)
            num = num.astype('float32')
            predict = model.predict(num, verbose=0)
            if np.amax(predict) < 0.15:
                predictions.append(0)
                continue
            predictions.append(np.argmax(predict))
        self.prediction = np.array(predictions).reshape(9, 9)
        self.prediction = np.flip(self.prediction, 0)
        self.prediction = np.flip(self.prediction, 1)
    
    def _show_number_examples(self, quatity=5):
        """
        Muestra ejemplos de los números
        """
        for i in range(quatity):
            index = random.randint(0, len(self.numbers))
            num = cv2.resize(self.numbers[index], (28, 28)) / 255
            plt.imshow(num, cmap='gray')
            plt.show()

    def get_sudoku(self):
        """
        Lee, prepara y predice el sudoku
        return: Sudoku
        """
        # self.model_engine.init() # Descomentar si se quiere entrenar/crear el modelo
        self.model_engine._load_model()
        self._prepare_image()
        self._split_numbers()
        self._predict_numbers(self.model_engine.model)
        return self.prediction
    