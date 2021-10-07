import json

import os

class User:

    def __init__(self,username,password,email):
            self.username = username
            self.password = password
            self.email = email
            

class UserRepositorty:

    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users  from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", encoding="utf-8") as file:
                users = json.load(file)
                # print(users)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user["username"], password = user["password"], email = user ["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user : User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("login yapıldı")
                break
    def logout(self):
            self.isLoggedIn = False
            self.currentUser = {}
            print("Çıkış yapıldı.")
    
    def identity(self):
        if self.isLoggedIn:
            print(f"username:{self.currentUser.username}")
        else:
            print("Giriş yapılmadı.")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        print(list)
        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(list,file,ensure_ascii=False)

repository = UserRepositorty()

while True:
    print("Menü".center(50, "*"))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseçiminiz: ')
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username,password,email)
            repository.register(user)
            print(repository.users)
        elif secim == "2":
            if repository.isLoggedIn:
                print("Zaten giris yapılmış.")
            else:
                username = input("username: ")
                password = input("password: ")
                repository.login(username,password)

        elif secim == "3":
           repository.logout()

        elif secim == "4":
           repository.identity()
        else:
            print("yanlış seçim")
