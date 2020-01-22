This project was bootstrapped with [Poetry](https://github.com/python-poetry/poetry).

## Introduction

This is project illustrates the basic single neuron neural network demonstrated by [`giant_neural_network`](https://www.youtube.com/user/LogicGodTV) in his [Beginner Introduction to Neural Networks YouTube series](https://www.youtube.com/playlist?list=PLxt59R_fWVzT9bDxA76AHm3ig0Gg9S3So). `giant_neural_network` demonstrates the innerworkings and details of a neural network. As such, he describes the math used for the activation function and the loss (cost) function. The merit is a deeper understanding of what neural networks are and what they're doing at each step as it learns to classify new feature sets. However, `giant_neural_network` also notes that there are machine learning libraries that handle the math once we understand what a neural network is, what its doing, and how we can effectively use it.

As such, this project demonstrates his example using the [PyTorch library](https://github.com/pytorch/pytorch).

## Getting Started

To get started, ensure Python 3.7 and Poetry are installed. After:

### Clone the Repository

This project does not have a production build. Obtain the source by cloning or downloading the repository. If you have git installed, run the following command:

`git clone https://github.com/weiluntong/IntroNN.git`

Otherwise, there is a green button at the top right that says "Clone or download" to obtain the source code.

### Navigate to the source directory

If you cloned the source code, simply `cd` into the directory you just cloned. If you downloaded the zip, you'll have to uncompress it first and then navigate to the directory in a terminal.

### Install dependencies

Run this command:

`poetry install`

and that's it. You're ready to run any of the available scripts.

## Available Scripts

In the project directory, you can run:

### `poetry run start`

Runs the app. You can modify the python files within the `intronn` directory to see different outputs at different stages.

## Learn More

You can learn more in the [Poetry documentation](https://python-poetry.org/docs/).

Python documentation can be found [here](https://docs.python.org/), and PyTorch documentation is [here](https://pytorch.org/docs/stable/).
