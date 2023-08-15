import string
import random
import mysql.connector as C

mytab=C.connect(host="localhost",user="root",passwd="",database='db1')
cur=mytab.cursor()

Characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    passwordlenght = int(input("How many letters long your password would be :"))

    random.shuffle(Characters)

    password = []

    for i in range(passwordlenght):
        password.append(random.choice(Characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

    sql = "INSERT INTO Passwords (password) VALUES (password)"
    val = (str(password))
    cur.execute(sql ,val)
    mytab.commit()

choice = input("Do you wnat to generate a password y/n: ")
if choice == "y" or choice == "Y":
    generate_password()
else:
    print("Finished")
    quit
