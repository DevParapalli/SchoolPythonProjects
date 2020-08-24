import ast
from pprint import pprint

with open('marks.dat') as read_file:
    student_dict = ast.literal_eval(read_file.read())

pprint(student_dict)