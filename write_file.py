import NNL.file_handling as file_handling
import NNL.data_cleaning as data_cleaning
import json
from pprint import pprint


spam_emails , ham_emails = file_handling.email_dict()

Spam_emails_Vector_list = []
Ham_email_vector_list = []

for spam_email in spam_emails.values():
    cleaned_spam_email_vector = data_cleaning.get_email_vector(spam_email)
    Spam_emails_Vector_list.append(cleaned_spam_email_vector)

for ham_email in ham_emails.values():
    cleaned_ham_email_vector = data_cleaning.get_email_vector(ham_email)
    Ham_email_vector_list.append(cleaned_ham_email_vector)

Spam_Ham_Vectors = {
    "spam_email" : Spam_emails_Vector_list ,
    "ham_emails" : Ham_email_vector_list
}

with open("Spam_Ham_Vectors_04.json", "w") as file:
        json.dump(Spam_Ham_Vectors, file)


print("Done")