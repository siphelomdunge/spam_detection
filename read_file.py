from pprint import pprint

file_path = 'Model_data_I_H_W.txt'
my_list = []

with open(file_path, 'r') as file:
    # Read all lines from the file into a list
    lines = file.readlines()
    
    # Process each line to remove newline characters and add to the list
for line in lines:
    my_list.append(line.strip()) 

print(my_list)