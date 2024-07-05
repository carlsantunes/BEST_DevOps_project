# BEST_DevOps_project

# Dataset
MNIST library

![MNIST dataset of written digits](MNIST.png)

# Model Description
In this code we solved the classification problem of detecting what number is written in a picture using keras tensorflow package in python. We use as input a MNIST black and white picture of a digit and output the detected number which is between 0 and 9.

We are using a multi layer perceptron, with RELU and sigmoid as actiovation functions.

To prevent overfitting we decided to implement EarlyStopping.

![Multi-layer perceptron for MNIST classification problem](model.png)
Image by Rukshan Pramoditha

# Metrics
Accuracy: 90%

# GitHub Actions

# Docker
- docker build -t digit-classification-app .
- docker push whorudude/best_devops_project:2.0.0
- docker images
- docker run digit-classification-app


# Authors
- Arina
- Carlos
- Maros
- Krisz
