filename = 'test2.txt'
test_text = 'this is a test'

with open(filename, 'w') as f:
    f.write('hello\n')
    f.close()

# NEVER PLACE PASSWORDS APIKEYS ENCRYPTION KEYS ETC INSIDE OF YOUR SOURCE CODE!!!
