import os
script_path = os.path.dirname(os.path.realpath(__file__))
# somewhat hackish method.
with open(script_path + os.path.sep + "read_file.txt", "r") as file:
    length = 0
    for line in file:
        length = length + len(line) + 1 #Since the trailing newline is removed in for line 
    print("Size of File = ",length)

# proper method
def file_size(file_name):
    stat_info = os.stat(file_name)
    return stat_info.st_size

print("File Size of {} in bytes is {}".format('read_file.txt', file_size(script_path + os.path.sep + "read_file.txt")))