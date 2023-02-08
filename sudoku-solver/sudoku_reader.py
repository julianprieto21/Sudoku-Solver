import cv2
import numpy as np
import tensorflow as tf
import imutils as im


def _get_perspective(img, location, height=900, width=900):
    """
    Acomoda tablero
    """
    # Toma una imagen y la locación que interesa. Devuelve la region seleccionada
    pts1 = np.float32([location[0], location[3], location[1], location[2]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Aplica algoritmo de transformación de perspectiva
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result


def _find_board(img):
    """
    Encuentra el tablero en una imagen
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 13, 20, 20)
    edged = cv2.Canny(bfilter, 30, 180)
    key_points = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = im.grab_contours(key_points)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]
    location = None
    # Encontrar contorno del rectángulo
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 15, True)
        if len(approx) == 4:
            location = approx
            break
    result = _get_perspective(img, location)
    return result


def _split_boxes(board, show_boxes):
    """
    Separa el tablero en 81 casillas
    """
    input_size = 28
    rows = np.vsplit(board, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            box = cv2.resize(box, (input_size, input_size)) / 255.0
            if show_boxes:
                cv2.imshow("Box", box)
                cv2.waitKey(50)
            boxes.append(box)
    return boxes


def predict(board, find_board=False, show_boxes=False, show_board=False):
    """
    Utiliza cada casillero y predice que número es
    """
    input_size = 28
    model = tf.keras.models.load_model("modelo.h5")
    if find_board:
        board = _find_board(board)   
    board = cv2.bitwise_not(board)
    board = cv2.resize(board, (252, 252))
    board = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    if show_board:
        cv2.imshow("board", board)
        cv2.waitKey(0)
    boxes = _split_boxes(board, show_boxes)
    boxes = np.array(boxes).reshape(-1, input_size, input_size, 1)

    # Predecir
    predicted_numbers = []
    prediction = model.predict(boxes, verbose=False)
    predictions = []
    for i in prediction:
        predictions.append(i)
        accuracy = np.amax(i)
        if accuracy > 0.95:
            index = np.argmax(i)
            predicted_number = index
        else:
            predicted_number = 0
        predicted_numbers.append(predicted_number)
    # Reshape la lista
    board_num = np.array(predicted_numbers).astype("uint8").reshape(9, 9)
    return board_num, predictions
