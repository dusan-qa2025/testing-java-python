import ssl
 
# povezivanje sa web stranicom koja koristi sertifikat
context = ssl.create_default_context()
with context.wrap_socket(socket, server_hostname='www.example.com') as s:
  # provera validnosti sertifikata
  cert = s.getpeercert()
  if cert:
    # ako je sertifikat autentičan, ispisujemo poruku o sigurnosti
    print("Connection is secure.")
  else:
    # ako sertifikat nije autentičan, ispisujemo poruku o opasnosti
    print("Warning: Connection is not secure.")