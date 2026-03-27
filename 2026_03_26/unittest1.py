def check_user(user_name, password):
    db_user_name = "admin"
    db_password = "12345"

    if user_name == db_user_name and password == db_password:
        return True
    return False

#postavaljanje poruke korisniku
def set_message(user_name):
    return f"Welcome, {user_name}!"

def test_check_user():
    if check_user("admin", "12345") == True:
        print("Test check user je prosao!")
    else:
        print("Test check user nije prosao!")

# Unit test za setovanje poruka
def test_set_message():
    if set_message("admin") == "Welcome, admin!":
        print("Test message je prosao!")
    else:
        print("Test message nije prosao!")

test_check_user()
test_set_message()

# Integracija

def login_system(user_name, password):
    # provera kredencijala

    if check_user(user_name, password):
        # ssetovanje poruka

        return set_message(user_name)
    else:
        return "Neispravni korisnicki podaci!"
    
def test_login_system():
    ispravno_kor_ime = "admin"
    ispravan_password = "12345"

    if login_system(ispravno_kor_ime, ispravan_password) == "Welcome, admin!":
        print("Login system test je prosao!")
    else:
        print("Login system test nije prosao!")
        
test_login_system()

