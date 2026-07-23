from abc import ABC, abstractmethod

class AccountBase(ABC):
    email = ""
    first_name = ""
    last_name = ""

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @abstractmethod
    def save(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

class Account(AccountBase):

    def save(self):
        # real logic to save user to DB
        pass
    

class AccountFake(AccountBase):

    accounts = []

    def save(self):
        # save users to in-memory list
        AccountFake.accounts.append(self)

    def test_account_creation():
        account1 = AccountFake("Ben", "Lord", "email1@email.com")
        account2 = AccountFake("Tom", "Scot", "email2@email.com")
        account3 = AccountFake("John", "Jordan", "email3@email.com")

        account1.save()
        account2.save()
        account3.save()

        if(len(AccountFake.accounts) != 3):
            print("Failed")
        elif(AccountFake.accounts[2].email != "email3@enmail.com"):
            print("Failed")
        else:
            print("OK")


            