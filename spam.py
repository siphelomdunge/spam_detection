import sys 
import json
from pprint import pprint
from NNL.data_cleaning import get_email_vector
import NNL.model as model
import NNL.open_file as open_file


def main():
    """This is Spam """

    file = sys.argv[1]
    #print(file)

    with open(file, 'r' ,errors="ignore") as file:
        content = file.read()

    Input_Hidden_weights , Input_Hidden_bias , Hidden_Output_weights , Output_Bias = open_file.Vector_fixtures()

    
    clean_email = get_email_vector(content)

    pred = model.Neural_Network(clean_email , Input_Hidden_weights , Input_Hidden_bias , model.ReLU , Hidden_Output_weights , Output_Bias , model.sigmoid)

    output_predict = pred * 100

    #print(output_predict)

    if output_predict < 33 :
        return "spam"
    else :
        return "notspam"
    

print(main())