from pprint import pprint
import json

with open('marks.dat') as read_file:
    student_dict = json.loads(read_file.read())

pprint(student_dict)