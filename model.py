# Now i create my model
import random
import math 
import string 
from pprint import pprint
import NNL.data_cleaning as data_cleaning 

def Initialize_weights_bias(email_vector):
    
    """Takes on any email vector fictures to initialize the structure number of layer and random weigths and bias 
    and returns Hidden layer weights in a list , Hidden layer bais in a list , Hidden_layer to Output weights and a 
    bias"""
    # >> Input --> [Hidden layer 1] --> Output
    
    #  I    W1     W2     W3
    # [1] [0.25 , 0,56 , 0,75] 
    # [0] [0.84 , 0.67 , 0,64] 
    # [1] [0.35 , 0.58 , 0.30] 

    # if the are 100 inputs every neuron will have 100 wights 
    # First layer will have 32 neurons so it will be a 32 * 101 = 3232 weights and 32 biases 
    #the ouput neuron will only be one so its just a list of 32 wiegths   
    # so its a list with 32 items(list) and each item has 100(weights) items

    input_features = len(email_vector)
    number_of_neurons = 128
    Hidden_layer_one = []
    weights_per_neuron = []
    bias = []
    output_wiegths = []


    # This creates a list(HIdden layer) of lists (eash list has 100 weights for every input) and 32 biases
    while len(Hidden_layer_one) != number_of_neurons :
        while len(weights_per_neuron) != input_features :
            num = random.uniform(-0.01, 0.01)
            weights_per_neuron.append(round(num,2))
        Hidden_layer_one.append(weights_per_neuron)
        weights_per_neuron = []
        bias.append(0)

    while len(output_wiegths) != number_of_neurons:
        output_weigth_num = random.uniform(-0.01, 0.01)
        output_wiegths.append(output_weigth_num)
    output_bias = 0
        
    return Hidden_layer_one , bias , output_wiegths , output_bias 


# Now we do the first pass through the network
def Neural_Network(email, Hidden_layer_weights, Hidden_layer_bias, act_fun, 
                   Output_weights, Output_bias, final_act_fun):
    """
    Passes an email (vectorized input) through the network and returns:
    - Hidden layer activations
    - Final predicted output
    """
    First_layer_output = []

    # ---- Hidden Layer ----
    for idx, neuron_weights in enumerate(Hidden_layer_weights):
        output_num = 0.0
        for i in range(len(email)):
            output_num += neuron_weights[i] * email[i]
        neuron_out = act_fun(output_num + Hidden_layer_bias[idx])
        First_layer_output.append(neuron_out)

    # ---- Output Layer ----
    final_sum = 0.0
    for i in range(len(First_layer_output)):
        final_sum += Output_weights[i] * First_layer_output[i]
    y_pred = final_act_fun(final_sum + Output_bias)

    return y_pred

    
#Now its time to train the model using Backpropagation 
def back_prob_output(output_pred , y_real , hidden_Output_weights , hidden_output_bias , act_neurons ):
    
    """ This is where we back propagate meaning we are updating every wait and every bias acorrding to how
     much the contribured to the loss starting with the predicted output going back wards """

    loss = loss_calculation(y_real,output_pred)
    
    #Derivative of loss with respect to the predicted value 
    der_loss_output = (output_pred - y_real)
    der_act_neuron_before_act = output_pred * (1 - output_pred)
    gradient_of_output_neuron = der_loss_output * der_act_neuron_before_act 
    gradient_of_bias_1 = gradient_of_output_neuron
    new_bias_1 = new_bias(hidden_output_bias, 0.01 , gradient_of_bias_1)

    new_weight_list = []


    for i in range(len(act_neurons)):
        #Gradient of every weight and bias 
        gradient_of_weight = gradient_of_output_neuron * act_neurons[i] 
    
        #Calculate every new Wights between hidden_layer and output
        new_weight_1 = new_weigth(hidden_Output_weights[i] , 0.01 , gradient_of_weight)
        new_weight_list.append(new_weight_1)


    return (new_weight_list , new_bias_1)
     
def back_prob_hidden(output_pred, y_real, hidden_output_weights, act_neurons,
                     input_hidden_weights, input_hidden_bias, inputs):
    """
    Backpropagate error from output layer to hidden layer.
    Update input-hidden weights and biases.
    """

    der_loss_output = (output_pred - y_real)
    new_input_weights = []
    new_input_bias = []

    for i in range(len(hidden_output_weights)):
        # Derivative of loss wrt hidden neuron activation
        dloss_act_neuron = hidden_output_weights[i] * der_loss_output

        # Derivative of hidden activation 
        dloss_of_activation = 1 if act_neurons[i] > 0 else 0

        # Total gradient of hidden neuron
        gradient_of_neuron = dloss_act_neuron * dloss_of_activation

        # Update each input weight for this neuron
        neuron_weights = []
        for j, w in enumerate(input_hidden_weights[i]):
            gradient = gradient_of_neuron * inputs[j]
            new_weight = new_weigth(w, 0.01, gradient)
            neuron_weights.append(new_weight)

        new_input_weights.append(neuron_weights)

        # Bias update
        gradient_of_bias = gradient_of_neuron
        new_b = new_bias(input_hidden_bias[i], 0.01, gradient_of_bias)
        new_input_bias.append(new_b)

    return new_input_weights, new_input_bias
     

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
    if x < -709:
        return 0.0
    elif x > 709:
        return 1.0
    return 1 / (1 + math.exp(-x))



# ham_email = data_cleaning.ham_vector_features()
# spam_email = data_cleaning.spam_vector_features()

# for value in spam_email:
#     for message in value :
#         init_message = message
#         break
#     break 

def init_state(init_email):
    """This is to calculate the first runs network state"""
    Hidden_layer_weights , Hidden_layer_bias , Hidden_output_weights , output_bias = Initialize_weights_bias(init_email)

    return (Hidden_layer_weights , Hidden_layer_bias , Hidden_output_weights , output_bias)


#neurons , predicted  = Neural_Network(checked_email_2 , Hidden_layer_weights, Hidden_layer_bias , ReLU, Hidden_output_weights , output_bias , sigmoid)

#New_input_hidden_weights , New_input_hidden_bias =back_prob_hidden(predicted , 1 , Hidden_output_weights ,neurons ,Hidden_layer_weights , Hidden_layer_bias , checked_email_2)
#New_hidden_output_weights , New_hidden_out_bias = back_prob_output(predicted , 1 , Hidden_output_weights ,output_bias , neurons )

#print(len(New_input_hidden_weights))
#print(len(New_input_hidden_bias))
#print(Hidden_output_weights)
#print(New_hidden_output_weights)
#print(New_hidden_out_bias)



        


