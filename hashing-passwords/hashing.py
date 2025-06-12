# hash - one-way (não da pra 'unhashar' uma palavra) function that obscure some kind of plain texte of password for example

import hashlib

pw = "Password123"

# whats a salt
# bcrypt roda apenas em bytes, então precisa dar encode na senha antes de mandar pra lá

hashed = hashlib.sha256(pw.encode()).hexdigest() # a função é hashpw independente do nome da variável

given = input('Please enter a password>> ')

is_correct = hashlib.sha256(given.encode()).hexdigest() == hashed

print(is_correct)