import NNL.model as model
import json
import random

def main():
    with open("Spam_Ham_Vectors_04.json", "r") as file:
        Spam_Ham_Vectors = json.load(file)

    spam_data = [(x, 1) for x in Spam_Ham_Vectors["spam_email"]]
    ham_data = [(x, 0) for x in Spam_Ham_Vectors["ham_emails"]]
    dataset = spam_data + ham_data

    # Initialize network
    input_hidden_weights, input_hidden_bias, Hidden_output_weights, output_bias = model.init_state(spam_data[0][0])

    epochs = 15
    for epoch in range(epochs):
        total_loss = 0
        random.shuffle(dataset)

        for email_vec, label in dataset:
            hidden, pred = model.Neural_Network(email_vec, input_hidden_weights, input_hidden_bias,
                                                model.sigmoid, Hidden_output_weights, output_bias, model.sigmoid)

            New_hidden_output_weights, New_hidden_out_bias = model.back_prob_output(pred, label, Hidden_output_weights, output_bias, hidden)
            New_input_hidden_weights, New_input_hidden_bias = model.back_prob_hidden(pred, label, Hidden_output_weights, hidden, input_hidden_weights, input_hidden_bias, email_vec)

            input_hidden_weights = New_input_hidden_weights
            input_hidden_bias = New_input_hidden_bias
            Hidden_output_weights = New_hidden_output_weights
            output_bias = New_hidden_out_bias

            total_loss += 0.5 * (label - pred)**2


        print(f"Epoch {epoch+1}/{epochs} | Loss: {round(total_loss, 4)}")


    # Save weights
    model_data = {
        "Input_Hidden_Weights": input_hidden_weights,
        "Input_Hidden_Bias": input_hidden_bias,
        "Hidden_Output_Weights": Hidden_output_weights,
        "Hidden_Output_Bias": output_bias
    }

    with open("trained_model_weights_04.json", "w") as file:
        json.dump(model_data, file)

if __name__ == "__main__":
    main()
