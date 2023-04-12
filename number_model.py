import random
import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class NumberModel:
    def __init__(self, dt_path, epochs=10, batch_size=32, validation_split=0.2, verbose=0, seed=242):
        self.path = dt_path
        self.dt = None
        self.model = None
        self.seed = seed
        self.epoch = epochs
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.verbose = verbose
        self.num_classes = 10
        self.input_shape = (28, 28, 1)
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.history = None
        self.model_optimizer = tf.keras.optimizers.Adam()
        self.model_loss = 'sparse_categorical_crossentropy'
        self.model_metrics = ['accuracy']
        self.model_layers = [
            tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=self.input_shape),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Dropout(0.25),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(self.num_classes, activation='softmax')
        ]

    def _init_dataset(self):
        self.dt = pd.read_csv(self.path)
        X = self.dt.drop(columns = {"names", "labels"}) / 255
        X = X.values.reshape(X.shape[0], 28, 28, 1)
        y  = self.dt["labels"].values.reshape((-1,))
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=self.seed)
        self.x_train = self.x_train.astype("float32")
        self.x_test = self.x_test.astype("float32")
        print("x_train shape:", self.x_train.shape)
        print("x_test shape:", self.x_test.shape)
        print("y_train shape:", self.y_train.shape)
        print("y_test shape:", self.y_test.shape)

    def _init_model(self):
        self.model = tf.keras.Sequential(self.model_layers)
        self.model.compile(loss=self.model_loss, optimizer=self.model_optimizer, metrics=self.model_metrics)
        self.model.summary()

    def _train_model(self):
        self.history = self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epoch,
                                      validation_split=self.validation_split, verbose=self.verbose)

    def _plot_history(self):
        plt.plot(self.history.history['accuracy'])
        plt.plot(self.history.history['val_accuracy'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()

    def _save_model(self):
        self.model.save("number_model.h5")

    def _load_model(self):
        self.model = tf.keras.models.load_model("number_model.h5")

    def _plot_example(self):
        index = random.randint(0, len(self.x_train))
        plt.imshow(self.x_train[index].reshape(28, 28), cmap='Greys')
        plt.show()

    def _predict_examples(self, quantity=5):
        for i in range(quantity):
            index = random.randint(0, len(self.x_test))
            predict = self.model.predict(self.x_test[index].reshape(1, 28, 28, 1), verbose=self.verbose)
            print(self.x_test[index].reshape(1, 28, 28, 1).shape)
            plt.imshow(self.x_test[index].reshape(28, 28), cmap='Greys')
            plt.title("Predicted: " + str(np.argmax(predict)))
            plt.show()

    def init(self):
        self._init_dataset()
        self._init_model()
        self._train_model()
        self._save_model()
