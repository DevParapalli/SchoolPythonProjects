with open('read_file.txt') as file:
    for line in file:
        print(line.strip())

# strip function removes excess whitespace
"""
without strip()

Line 01 *

Line 02 **

Line 03 ***

Line 04 ****

Line 05 *****
"""
"""
with strip()
Line 01 *
Line 02 **
Line 03 ***
Line 04 ****
Line 05 *****
"""