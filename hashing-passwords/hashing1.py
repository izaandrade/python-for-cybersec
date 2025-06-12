import bcrypt

pw = "Password123"

hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

given = input('Please enter a password ')

is_correct = bcrypt.checkpw(given.encode(), hashed)

print(is_correct)