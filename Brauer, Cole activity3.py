#Create a program that has the user create their own username
#and password and allows them to type "lock", and only accepts
#their name and password to lock

print("Loading...")
import time
time.sleep(2)
print("Do I get extra marks for this?")
time.sleep(1)
print("Welcome, please create an account to proceed")
username = input("UserName: ")
password = input("Password: ")
print("To log off, type lock.")
command = None
username1 = None
password1 = None
while command != "lock":
    command = input("What would you like to do?: ")
while username1 != username:
    print("Please log in")
    username1 = input("Username: ")
while password1 != password:
    password1 = input("Password: ")
print("Welcome back,", username)
time.sleep(1)
print("Goodbye")
time.sleep(1)
