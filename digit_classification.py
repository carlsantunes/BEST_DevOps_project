from keras.utils import to_categorical
from keras.layers import Dense
from keras.models import Sequential
from keras.callbacks import EarlyStopping
from keras.datasets import mnist
import numpy as np


def normalize(values: np.ndarray) -> float:
    return values / 255


def run() -> float:
    # Getting the MNIST dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_test, y_test = np.array(x_test), np.array(y_test)
    print("Train dataset size:", len(x_train))
    print("Test dataset size:", len(x_test))

    # Convert the 28x28 array to a 784 length vector
    # (convolutional networks probably would work better)
    x_test = x_test.reshape(x_test.shape[0], -1)
    x_train = x_train.reshape(x_train.shape[0], -1)

    # Normalize dataset: 0-255 to 0.0-1.0
    x_train = normalize(x_train)
    x_test = normalize(x_test)

    # One-hot encoding
    num_classes = 10
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    # Building the net structure
    model = Sequential()
    model.add(Dense(5, activation='relu', input_shape=(28 * 28,)))
    model.add(Dense(10, activation='sigmoid'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Start training
    es = EarlyStopping(monitor='val_loss', min_delta=1e-4, patience=5, verbose=1, restore_best_weights=True)

    history = model.fit(x_train, y_train, epochs=15,
                        batch_size=32,
                        validation_data=(x_test, y_test),
                        verbose=1,
                        callbacks=[es])

    # Test model
    score = model.evaluate(x_test, y_test, verbose=1) * 100
    score = score[1] * 100
    print(f"Prediction accuracy: {score:.2f}%")
    return score


if __name__ == "__main__":
    run()
