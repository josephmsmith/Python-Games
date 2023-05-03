pwd = input("What is master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            values = data.split("|")
            if len(values) == 2:
                user, passw = values
                print("User: ", user, "| Password: ", passw)
            else:
                print("Invalid data format:", data)


def addem():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones?(view, add) q to quit: " )
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        addem()
    else:
        print("Invalid mode.")
        continue


