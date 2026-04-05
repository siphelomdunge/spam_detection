# This is where we open file and read text 

import os
from pprint import pprint

def read_file(path):
    with open(path, 'r', errors="ignore") as file: 
        return file.read()
         
def email_dict():
    spam_files_content = {}
    ham_files_content = {}

    spam_folder_contents = os.listdir("/home/siphelo/WTC_25/spam_detection/enron1/spam")
    #spam_folder_contents = os.listdir("C:/Users/sipma/WTC_25/spam_detection/enron1/spam")
    ham_folder_contents = os.listdir("/home/siphelo/WTC_25/spam_detection/enron1/ham")
    #ham_folder_contents = os.listdir("C:/Users/sipma/WTC_25/spam_detection/enron1/ham")


    for file_name in spam_folder_contents:
        spam_files_content[file_name] = read_file(f"./enron1/spam/{file_name}")
                
    for file_name_2 in ham_folder_contents:
        ham_files_content[file_name_2] = read_file(f"./enron1/ham/{file_name_2}")
        
    return (spam_files_content , ham_files_content)



if __name__ == "__main__":
    pprint(email_dict()[1])