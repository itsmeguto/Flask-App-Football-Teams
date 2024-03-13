from werkzeug.security import generate_password_hash

# Replace 'your_password_here' with the actual password you want to hash
password_hash = generate_password_hash('viewer')
print(password_hash)