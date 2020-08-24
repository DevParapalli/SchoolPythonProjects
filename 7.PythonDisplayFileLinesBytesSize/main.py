# somewhat hackish method.
with open("read_file.txt", "rb") as file:
    length = 0
    for line in file:
        print(line)
        length = length + len(line)
    print("Size of File = ",length)

# proper method
def file_size(file_name):
    try:
        print(os)
    except:
        import os
    stat_info = os.stat(file_name)
    return stat_info.st_size

print("File Size of {} in bytes is {}".format('read_file.txt', file_size('read_file.txt')))