# MNIST Handwriting Recognition

This repository contains two Python scripts for creating and training a Convolutional Neural Network (CNN) to recognize handwritten digits using the MNIST dataset. It is designed as a beginner-friendly project, and the following files are included:

1. `mnist.py`: This script provides a simple graphical user interface (GUI) for drawing handwritten digits and using the trained model to predict them. It uses the TensorFlow library for deep learning and tkinter for the GUI.

2. `train.py`: This script trains a CNN model on the MNIST dataset and saves the trained model as `mnist_model.h5`. You can use this model with the `mnist.py` script for digit recognition.

## Requirements

To run the `mnist.py` and `train.py` scripts, you need to have the following Python libraries installed:

- TensorFlow
- tkinter
- numpy
- PIL (Pillow)
- matplotlib

You can install these libraries using pip with the following command:

```bash
pip install tensorflow tkinter numpy pillow matplotlib
