from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def update():
    name = input('Account Name need to update: ')
    pwd = input('Updated Password need to update : ')
    count = 0
    with open('passwords.txt', 'r') as f:
        read_file=f.readlines()
        print(read_file)
        for line in read_file:
            data = line.rstrip()
            user, passw = data.split("|")
            if user == name:
                read_file[count]=name + "|" + fer.encrypt(pwd.encode()).decode() + "\n"
                print("user present")
                print(read_file , "looop read file")
                count +=1
            else:
                count += 1

    with open('passwords.txt', 'w') as write_mode:
        write_mode.writelines(read_file)

def remove():
    name = input('Account Name need to Delete: ')
    with open('passwords.txt', 'r') as f:
        read_file = f.readlines()
        with open('passwords.txt', 'w') as delete_mode:
            for line in read_file:
                data = line.rstrip()
                user, passw = data.split("|")
                if user == name:
                    print("User present so deleted the user")
                else:
                    delete_mode.write(line)

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add,update,delete), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "update":
        update()
    elif mode == "delete":
        remove()
    else:
        print("Invalid mode.")
        continue