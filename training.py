# This is wehere i train the model 
import NNL.model as model 
import NNL.data_cleaning as data_cleaning
import json
import random

def main():
    
    with open("Spam_Ham_Vectors.json", "r") as file:
        Spam_Ham_Vectors = json.load(file)

    Spam_emails_Vector_list = Spam_Ham_Vectors["spam_email"]
    Ham_email_vector_list = Spam_Ham_Vectors["ham_emails"]



    # We first initialize the start of the network before any prediction 
    input_hidden_weights , input_hidden_bias , Hidden_output_weights , output_bias = model.init_state(Spam_emails_Vector_list[0])

    email_index = 0


    while email_index != len(Ham_email_vector_list):
        # #Run Through the network
        # random.shuffle(Spam_emails_Vector_list)
        # random.shuffle(Ham_email_vector_list)
        spm_email = Spam_emails_Vector_list[email_index]
        Hidden_layer_Neurouns , prediction = model.Neural_Network(spm_email, input_hidden_weights , input_hidden_bias , model.ReLU , Hidden_output_weights , output_bias , model.sigmoid)

        #Back propagate updating weights and bias
        New_hidden_output_weights , New_hidden_out_bias = model.back_prob_output(prediction , 1 , Hidden_output_weights , output_bias , Hidden_layer_Neurouns)
        New_input_hidden_weights , New_input_hidden_bias = model.back_prob_hidden(prediction , 1 , Hidden_output_weights , Hidden_layer_Neurouns , input_hidden_weights , input_hidden_bias , spm_email)

        #Update Old variables 
        input_hidden_weights = New_input_hidden_weights
        input_hidden_bias = New_input_hidden_bias
        Hidden_output_weights = New_hidden_output_weights
        output_bias = New_hidden_out_bias
        
        pred_percent = prediction * 100

        print(f"Current prediction: {round(pred_percent , 2)} On epoch: {email_index} for spam" )

        hm_email = Ham_email_vector_list[email_index]
        Hidden_layer_Neurouns , prediction = model.Neural_Network(hm_email, input_hidden_weights , input_hidden_bias , model.ReLU , Hidden_output_weights , output_bias , model.sigmoid)

        #Back propagate updating weights and bias
        New_hidden_output_weights , New_hidden_out_bias = model.back_prob_output(prediction , 0, Hidden_output_weights , output_bias , Hidden_layer_Neurouns)
        New_input_hidden_weights , New_input_hidden_bias = model.back_prob_hidden(prediction , 0 , Hidden_output_weights , Hidden_layer_Neurouns , input_hidden_weights , input_hidden_bias , hm_email)

        #Update Old variables 
        input_hidden_weights = New_input_hidden_weights
        input_hidden_bias = New_input_hidden_bias
        Hidden_output_weights = New_hidden_output_weights
        output_bias = New_hidden_out_bias

        pred_percent = prediction * 100

        print(f"Current prediction: {round(pred_percent , 2)} On epoch: {email_index} for ham" )

        email_index += 1



    # 1. Create a dictionary to hold everything
    model_data = {
        "Input_Hidden_Weights":New_input_hidden_weights,
        "Input_Hidden_Bias": New_input_hidden_bias,
        "Hidden_Output_Weights": New_hidden_output_weights,
        "Hidden_Output_Bias": New_hidden_out_bias
        }

    # 2. Open file and write as JSON
    with open("practice_model_weights.json", "w") as file:
        json.dump(model_data, file)



if __name__ == "__main__":
    main()