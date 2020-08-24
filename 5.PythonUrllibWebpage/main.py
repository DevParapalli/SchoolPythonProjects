import urllib.request

url_file = urllib.request.urlopen('http://www.example.com')
for line in url_file:
    print(line.decode().strip())

# urllib gets the content of the page as a bytes object.
# to print it safely, we decode it.
# the strip function removes excess whitespaces in the string.
