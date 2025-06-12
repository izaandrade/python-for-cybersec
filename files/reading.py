filename = 'test.txt'
test_text = 'this is a test'

lines = []

f = open(filename, 'r') # f is now an object
# w mode means that everything in that file will be overwritten
# a mode means append to the end  of the file
# r for read mode
lines = f.readlines()
f.close() # ALWAYS CLOSE THE FILE THAT YOU ARE EDITING!!!

for line in lines:
    print(line)