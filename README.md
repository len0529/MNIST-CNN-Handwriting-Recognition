# MNIST Handwriting Recognition

This repository contains two Python scripts for creating and training a Convolutional Neural Network (CNN) to recognize handwritten digits using the MNIST dataset. It is designed as a beginner-friendly project, and the following files are included:

本存儲庫包含兩個Python腳本，用於創建和訓練卷積神經網絡（CNN）以使用MNIST數據集識別手寫數字。這是一個適合初學者的項目，包括以下文件：

1. `mnist.py`: This script provides a simple graphical user interface (GUI) for drawing handwritten digits and using the trained model to predict them. It uses the TensorFlow library for deep learning and tkinter for the GUI.

   `mnist.py`腳本提供了一個簡單的圖形用戶界面（GUI），用於繪製手寫數字並使用已訓練的模型進行預測。它使用TensorFlow庫進行深度學習，使用tkinter進行GUI。

2. `train.py`: This script trains a CNN model on the MNIST dataset and saves the trained model as `mnist_model.h5`. You can use this model with the `mnist.py` script for digit recognition.

   `train.py`腳本在MNIST數據集上訓練了一個CNN模型，並將訓練好的模型保存為`mnist_model.h5`。您可以將此模型與`mnist.py`腳本一起用於數字識別。

## Requirements (要求)

To run the `mnist.py` and `train.py` scripts, you need to have the following Python libraries installed:

要運行`mnist.py`和`train.py`腳本，您需要安裝以下Python庫：

- TensorFlow
- tkinter
- numpy
- PIL (Pillow)
- matplotlib

You can install these libraries using pip with the following command:

您可以使用以下命令使用pip安裝這些庫：

```bash
pip install tensorflow tkinter numpy pillow matplotlib
