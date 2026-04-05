##Spam detaction##

>> My program will be devided into 4 parts the reading of text from files , clean the text (renmove punctuations , stop words , convert every word to lowercase)  

1) Read text from file
    ...

2) clean the data 
    ...

3) create features like recording if certain words are there
    ...

4) Building the model and training the model
    # I will be building a Neural Network model #
        >> Input --> [Hidden layer 1] --> [Hidden layer 2] --> Output
        1) Input is the data categorized the number of neurons will be determined by  the amount of vectors i have e,g 3 if i have is free present , is click present , or is urgent present so will have a list like [1,0,0] 1 for yes and 0 for now
        2) will first initialize the weights randomlly they will be between 0 and 1 and a random bias so if we have 2 neurons will have 3 list with 3 weights each [0.4 , 0.65 , 1] [ 0,6 , 0,7 , 0] and each a bias so the input to the first layer would be  output = ReLU(1*0.4 + 0*0.65 + 0*1) + 0.45 same for the second neuron the we end up with someting like [0.63 , 0.70] which will be the input to our next layer our output which predicts if its a spam or not(number of neuron in hidden layer could start a 5-10) the output layer will countain one neuron which determines the spam or not spam  
        3) Ater determing the output now its time to implement the loss function(Measure how well the network performes by comparing predicted output to actual input...Compare Prediction with Real Answer (Label):
        Suppose the real label is spam = 1. Error = (1 - 0.3) = 0.7)
        4) Now we backpropagate The network calculates how much each weight contributed to the error. This uses calculus (gradients) 
        5) We than Update Weights (Gradient Descent): Each weight is adjusted a tiny bit in the direction that reduces the error.(new_weight = old_weight - learning_rate × gradient)
        6) This happens for every weight in the first layer too.
        Over many training steps, the weights shift from random values to meaningful patterns.

        

