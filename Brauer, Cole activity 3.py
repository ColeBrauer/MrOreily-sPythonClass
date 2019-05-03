# create a program that has the user create their own username and
# password and allows them to type "lock", and only accepts
# their name and password to unlock
print("Create a username")
username = input("Username:")
print("Create a password:")
password = input("Password")
print("hold on, creating account...")

print("log in:")
input(username)
password = str()
while password != password:
    password = input("password:")
    print("Hello,:", username)
    
