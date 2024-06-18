from cryptography.fernet import Fernet

def write_key():
    """
    Generates a new key and saves it into a file named 'key.key'.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the 'key.key' file.
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Ensure the key is loaded only once
key = load_key()
fer = Fernet(key)

def view():
    """
    Decrypts and prints all stored passwords.
    """
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if data:  # Ensure the line is not empty
                    user, passw = data.split("|")
                    decrypted_password = fer.decrypt(passw.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_password}")
    except FileNotFoundError:
        print("No passwords file found. Add a password first.")

def add():
    """
    Adds a new account name and password to the 'passwords.txt' file.
    """
    name = input('Account Name: ')
    pwd = input('Password: ')
    encrypted_password = fer.encrypt(pwd.encode()).decode()
    
    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{encrypted_password}\n")

def main():
    """
    Main loop to prompt user for adding or viewing passwords.
    """
    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == 'q':
            break
        elif mode == 'view':
            view()
        elif mode == 'add':
            add()
        else:
            print("Invalid mode. Please enter 'view', 'add', or 'q'.")

if __name__ == "__main__":
    main()
