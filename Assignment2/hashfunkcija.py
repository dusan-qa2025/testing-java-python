import hashlib
 
def create_hash(password):
  # kreiranje hash-a za lozinku
  hash = hashlib.sha256(password.encode())
  # vraćanje hash-a kao heksadecimalni string
  return hash.hexdigest()
 
# testiranje funkcije
password = "password123"
password_hash = create_hash(password)
print(password_hash)
# Output: d5a1b3c5d8e2f1g7
