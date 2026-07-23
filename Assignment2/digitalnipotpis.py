import hashlib
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
 
# kreiranje ključeva
private_key = rsa.generate_private_key(
  public_exponent=65537,
  key_size=2048
)
public_key = private_key.public_key()
 
# serijalizacija ključeva
private_key_pem = private_key.private_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PrivateFormat.PKCS8,
  encryption_algorithm=serialization.NoEncryption()
)
public_key_pem = public_key.public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
)
 
# funkcija za potpisivanje dokumenta
def sign_document(document, private_key):
  # kreiranje hash-a dokumenta
  document_hash = hashlib.sha256(document.encode()).digest()
  # potpisivanje dokumenta pomoću privatnog ključa
  signature = private_key.sign(
    document_hash,
    padding.PSS(
      mgf=padding.MGF1(hashes.SHA256()),
      salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
  )
  # enkodiranje potpisa u base64
  return base64.b64encode(signature).decode()
 
# funkcija za proveru potpisa
def verify_signature(document, signature, public_key):
  # dekodiranje potpisa iz base64
  signature = base64.b64decode(signature.encode())
  # kreiranje hash-a dokumenta
  document_hash = hashlib.sha256(document.encode()).digest()
  # provera potpisa pomoću javnog ključa
  try:
    public_key.verify(
      signature,
      document_hash,
      padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
      ),
      hashes.SHA256()
    )
    # ako provera uspe, vraća se True
    return True
  except:
    # ako provera ne uspe
        return False

