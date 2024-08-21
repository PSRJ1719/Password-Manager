# Password Manager

This Python script is a simple password manager that securely stores and retrieves passwords. It uses the `cryptography` library's `Fernet` encryption to protect your passwords by encrypting them before storing them in a text file.

## Features

- **Password Encryption:** Encrypts passwords before saving them to ensure they are securely stored.
- **Password Decryption:** Decrypts and displays passwords when requested.
- **Key Management:** Generates a unique encryption key, which is stored in a file and used to encrypt and decrypt the passwords.
- **Simple User Interface:** Command-line interface for adding new passwords and viewing stored passwords.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python package: `cryptography`

You can install the required package using pip:

pip install cryptography

## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine using the following command:

   git clone https://github.com/PSRJ1719/Password-Manager.git

2. **Navigate to the Script Directory:**

   Navigate to the directory where the script is located:

   cd Password-Manager

3. **Run the Script:**

   You can run the script using the following command:

   python password_manager.py

4. **Commands:**

   After running the script, you will be prompted to add or view passwords:

   - **Add a Password:**
     - Choose the 'add' option to add a new account name and password.
     - The password will be encrypted and stored in the `passwords.txt` file.
     - Example:

       Would you like to add a new password or view existing ones (view, add), press q to quit? add
       Account Name: Gmail
       Password: mypassword123

   - **View Stored Passwords:**
     - Choose the 'view' option to decrypt and display all stored passwords.
     - Example:

       Would you like to add a new password or view existing ones (view, add), press q to quit? view
       User: Gmail | Password: mypassword123

   - **Quit the Script:**
     - Press 'q' to quit the program.

5. **Key Management:**

   - The first time you run the script, it will generate a unique encryption key and store it in a file named `key.txt`.
   - This key is crucial for decrypting your passwords, so do not delete the `key.txt` file.
   - If the `key.txt` file is lost, any encrypted passwords will be irretrievable.

6. **Example Output:**

   - **Adding a Password:**

     Account Name: Gmail
     Password: mypassword123

   - **Viewing Stored Passwords:**

     User: Gmail | Password: mypassword123


## Security Considerations

- **Encryption Key:** The encryption key stored in `key.txt` is critical to the security of your passwords. Ensure that this file is stored securely and is not shared with anyone.
- **Password Storage:** The encrypted passwords are stored in `passwords.txt`. While they are encrypted, you should still keep this file in a secure location to prevent unauthorized access.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
