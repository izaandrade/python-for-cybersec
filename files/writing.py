filename = 'test.txt'
test_text = 'this is a test and '

f = open(filename, 'a') # f is now an object
# w means that everything in that file will be overwritten
# a means append to the end  of the file
f.write(test_text)
f.write('this is line one\n')
f.write('this is line two\n')
for i in range(10):
    f.write(f'number {i}\n')
f.close() # ALWAYS CLOSE THE FILE THAT YOU ARE EDITING!!!
