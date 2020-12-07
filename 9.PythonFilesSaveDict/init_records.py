# do not  run this file if you want to keep the data inside the marks.json
import json
# we will start with some initial data 
# roll_number is of the format <class_code>_<student_id>
student_dict = {
    "12_9001":{'Name':"Dummy9001", "Marks":10},
    "12_9002":{'Name':"Dummy9002", "Marks":11},
    "12_9003":{'Name':"Dummy9003", "Marks":12},
    "12_9004":{'Name':"Dummy9004", "Marks":13},
    "12_9005":{'Name':"Dummy9005", "Marks":14},
}

# we will operate on the dict first then write that to the json file

no_of_iterations = int(input("Enter the no of record to be entered:"))

for i in range(no_of_iterations):
    print("Current Iter: ", i)
    roll_num = input("Enter Roll Number: ")
    name = input("Name: ")
    marks = input("Marks: ")
    student_dict[roll_num] = {'Name':name, 'Marks':marks}

with open("marks.json", "w+") as write_file:
    input('This will overwrite all data in the marks.json. CTRL + C to exit')
    write_file.write(json.dumps(student_dict))


