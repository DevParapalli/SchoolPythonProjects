# defining 3 file objects
# one read and 2 write

og_file = open("og_file.txt")
a_file = open("a_file.txt", "w")
removed_a = open("removed_a.txt", "w")

for line in og_file:
    if line.find('a') != -1:
        a_file.write(line)
    else:
        removed_a.write(line)

# og file has the data to be sorted 
# a_file has the lines with the char a
# removed_a has the text with all instances of char a removed
