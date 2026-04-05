# Now i create my model
import random
import math 
import string 
from pprint import pprint
import data_cleaning 

def Initialize_weights_bias(email , label):
    # >> Input --> [Hidden layer 1] --> [Hidden layer 2] --> Output
    
    # [0.25 , 0,56 , 0,75] [1]
    # [0.84 , 0.67 , 0,64] [0]
    # [0.35 , 0.58 , 0.30] [1]

    # if the are 100 inputs every neuron will have 100 wights 

    # First layer will have 32 neurons so it will be a 32 * 101 = 3200 weights and 32 biases 
    

    #the ouput neuron will only be one so its just a list of 32 wiegths   

    # so its a list with 64 items and each item has 100 items

    input_features = len(email)
    number_of_neurons = 32 
    Hidden_layer_one = []
    weights_per_neuron = []
    bias = []
    output_wiegths = []


    # This creates a list(HIdden layer) of lists (eash list has 100 weights for every input) and 32 biases
    while len(Hidden_layer_one) != number_of_neurons :
        while len(weights_per_neuron) != input_features :
            num = random.uniform(-1, 1)
            weights_per_neuron.append(round(num,2))

        Hidden_layer_one.append(weights_per_neuron)
        weights_per_neuron = []

        bias_num = random.uniform(-0.5, 0.5)
        bias.append(round(bias_num , 2))

    while len(output_wiegths) != number_of_neurons:
        output_weigth_num = random.uniform(-1, 1)
        output_wiegths.append(output_weigth_num)

    output_bias = round(random.uniform(-0.5, 0.5) , 2)
        
    return Hidden_layer_one , bias , output_wiegths , output_bias 

# the output for every neuron is calculated as output = activation(w1X1 + w2x2 ... w100X100)

# now we do the first pass through the network
def Neural_Network(email , Hidde_layer_weigths, Hidde_layer_bias, act_fun ,  Output_weights , Output_bias , final_act_fun ):

    # if we have 
    # input = [1,0,1]
    # weights_per_neuron = [ [0.25 , 0.56 , 0.75]
    #                        [0.84 , 0.67 , 0,64] 
    #                        [0.35 , 0.58 , 0.30] ] 
    #bias = [0.98 , 0.45 , 0,60]

    # the output of the first neuron is calculated: O = activation_funtion(0.25*1 + 0.56*0 + 0.75*1)+ 0.98 

    # this holds output of the calculatons in the end it must be of length = to num of neurons in a layer
    First_layer_output = []
    bias_index = 0
    output_num = 0
    num = 0

    #While we have not calculated the output of every neuron 
    while len(First_layer_output) != len(Hidde_layer_bias):
        #Take every neuron wiegths 
        for neuron in Hidde_layer_weigths:
            #use the length of the input to calculate the output pass is through an actication function
            #Append the output to the the list of the hiden_layer  
            for i in range(len(email)) :
                output_num += neuron[i]*email[i]

            neuron_num =act_fun(output_num + Hidde_layer_bias[bias_index])
            First_layer_output.append(round(neuron_num , 2))
            bias_index += 1


    # Now its where the model predicts if reducing all the neural network to one output
    for i in range(len(First_layer_output)):
        num += Output_weights[i] * First_layer_output[i]

    return final_act_fun(num + Output_bias)
    
#Now its time to train the model using Backpropagation 
def back_prob_output(output_pred , y_real , hidden_Output_weights , hidden_output_bias , act_neurons ):
    
    #This is For updatin the weights between the hidden layer and output
    #Derivative of loss with respect to the predicted value 
    der_loss_output = (output_pred - y_real)
    der_act_neuron_before_act = output_pred * (1 - output_pred)
    gradient_of_output_neuron = der_loss_output * der_act_neuron_before_act 
    gradient_of_bias_1 = gradient_of_output_neuron
    new_bias_1 = new_bias(hidden_output_bias, 0.001 , gradient_of_bias_1)

    new_weight_list = []


    for i in range(len(act_neurons)):
        #Gradient of every weight and bias 
        gradient_of_weight = gradient_of_output_neuron * act_neurons[i] 
    
        #Calculate every new Wights between hidden_layer and output
        new_weight_1 = new_weigth(hidden_Output_weights[i] , 0.01 , gradient_of_weight)
        new_weight_list.append(new_weight_1)


    return (new_weight_list , new_bias_1)
     
     
def back_prob_hidden(output_pred , y_real, hidden_output_weights, act_neurons, input_hidden_weights , input_hidden_bias , inputs):

    #Now we calculate the Gradients of the weights between the input and the hidden layer
    der_loss_output = (output_pred - y_real)
    input_count = 0
    new_input_weights = []
    new_input_bias = []
    wiegths_per_neuron = []


    for i in range(len(hidden_output_weights)):
        dloss_act_neuron = hidden_output_weights[i] * der_loss_output
        dloss_of_activation  = act_neurons[i] * (1 - act_neurons[i])
        gradient_of_neuron  = dloss_act_neuron * dloss_of_activation

        for w in input_hidden_weights[0]:
            gradient = gradient_of_neuron * inputs[input_count]
            gradient_of_bias = gradient_of_neuron

            new_weight_2 = new_weigth( w , 0.001 , gradient)
            new_input_weights.append(new_weight_2)
        wiegths_per_neuron.append[new_input_bias]
        new_input_bias =[]
        
        new_bias_2 = new_bias(input_hidden_bias[i], 0.001 , gradient_of_bias)
        new_input_bias.append(new_bias_2)

    return (wiegths_per_neuron , new_input_bias)

# This tells the network how wrong the prediction was 
def loss_calculation(y_true , y_pred):
    return 0.5 * (y_true - y_pred)**2


def new_weigth(old_weigth , learning_rate , gradient):
    return old_weigth - (learning_rate * gradient)

def new_bias(old_bias , learning_rate , bias_gradient):
    return old_bias - (learning_rate * bias_gradient)

def ReLU(x):
    if x > 0:
        return x
    else:
        return 0

def sigmoid(x):
    num = round(x , 2)
    if num < -709:
        return 0.0
    elif x > 709:
        return 1.0
    return 1 / (1 + math.exp(-num))

ham_email = data_cleaning.ham_vector_features()
spam_email = data_cleaning.spam_vector_features()

for value in ham_email.values():
    for message in value :
        init_message = message
        break
    break 


Hidden_layer , bias , Output_weight , Output_bias = Initialize_weights_bias(init_message,"spam")

count = 0
total_messages = 0

for value in ham_email.values():
    for message in value :
        checked_email = message
        is_not_spam = Neural_Network(checked_email, Hidden_layer, bias , ReLU, Output_weight , Output_bias , sigmoid) * 100
        if is_not_spam < 50 :
            count += 1
        total_messages += 1

count_two = 0
total_messages_two = 0

for value_mes in spam_email.values():
    for message in value_mes :
        checked_email_2 = message
        is_spam = Neural_Network(checked_email_2 , Hidden_layer, bias , ReLU, Output_weight , Output_bias , sigmoid) * 100
        if is_spam > 50 :
            count_two += 1
        total_messages_two += 1

predict_percent = (count / total_messages) * 100 
print(f"{predict_percent : 2f}% reported as not spam")


predict_percent_two = (count_two / total_messages_two) * 100 
print(f"{predict_percent_two : 2f}% reported as spam")

        

# for value in spam_email.values():
#     for message in value :
#         checked_email_2 = message
#         break

#print(checked_email)
#print(checked_email_2)

#print("Not_spam")
# print
# print("Spam")
# print(Neural_Network(checked_email_2, Hidden_layer, bias , ReLU, Output_weight , Output_bias , sigmoid))


# print("Not_spam")
# print
# print("Spam")
# print(Neural_Network(checked_email_2, Hidden_layer, bias , ReLU, Output_weight , Output_bias , sigmoid))
