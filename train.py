import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# 加載MNIST數據集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 重新整形和正規化圖像
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# 轉換整數標籤為one-hot編碼
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 創建CNN模型
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 訓練模型
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

# 保存模型
model.save('mnist_model.h5')

print("模型已保存為 'mnist_model.h5'")
