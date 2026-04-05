Overview

This project is a custom-built machine learning model designed to classify text messages or emails as either "spam" or "ham" (normal). Instead of relying entirely on pre-built high-level machine learning libraries, this project implements a Neural Network from scratch to demonstrate a deep understanding of natural language processing (NLP) and forward/backward propagation algorithms.

Project Workflow
The system pipeline is divided into four primary stages:

1. Data Ingestion
Reads and loads raw text data from local files into the environment for processing.

2. Text Preprocessing
Cleans the raw text data to improve model accuracy by:

Converting all characters to lowercase.

Removing standard punctuation.

Filtering out common stop words that do not contribute to the spam/ham classification.

3. Feature Engineering
Transforms the cleaned text into numerical format (feature vectors).

The model checks for the presence of specific high-risk "trigger" words (e.g., free, click, urgent) and translates these occurrences into binary or frequency-based inputs for the network.

4. Model Architecture & Training
The core of the project is a multi-layer Neural Network structured as follows:
Input Layer --> [Hidden Layer 1] --> [Hidden Layer 2] --> Output Layer

Training Process:

Initialization: The network categorizes the input based on the size of the feature vectors. Synaptic weights are initialized randomly between 0 and 1, alongside a random bias.

Forward Pass: The data passes through the network to generate a prediction (e.g., outputting 0.3 for a text).

Loss Calculation: A loss function measures the network's performance by comparing the predicted output to the actual label (e.g., if the real label is Spam 1, the error is 1 - 0.3 = 0.7).

Backpropagation: Utilizing calculus and gradients, the network calculates how much each individual weight contributed to the overall error.

Gradient Descent (Weight Update): Each weight is adjusted in the direction that reduces the error using the formula: new_weight = old_weight - (learning_rate × gradient).

Over multiple training iterations (epochs), the weights shift from random initialization to meaningful patterns, allowing the model to accurately identify spam.

Technologies Used
Python 

How to Run
Clone the repository:

Bash
git clone git@github.com:yourusername/your-repo-name.git
Navigate to the directory:

Bash
cd your-repo-name
Run the main script:

Bash
python spam.py

Author
Siphelo Mdunge

Email: mdunges22@gmail.com

GitHub: @siphelomdunge
