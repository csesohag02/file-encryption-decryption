# File Encryption and Decryption
## Overview
This Python script allows to encrypt and decrypt text files using the **Fernet encryption** algorithm from the `cryptography` library. It provides secure and easy-to-use functionality for file encryption and decryption.

## Features
- **Generate Key**: Create a key for encryption and decryption and save it to a file (`key.key`).
- **Encrypt File**: Encrypt the contents of a text file and save it as a new file.
- **Decrypt File**: Decrypt an encrypted file and restore the original content.

## Requirements
- Python 3.6 or higher
- `cryptography` library

## Installation
1. Clone or download this repository.
2. Install the required library using pip:
   ```bash
   pip install cryptography
   ```

## Usage
Run the script in your terminal:
```bash
python file_encrypt_decrypt.py
```

### Menu Options
1. **Generate Key**
   - Creates a key and saves it to `key.key`. This key is required for encryption and decryption.
2. **Encrypt File**
   - Input the name of the file you want to encrypt.
   - Specify an output file name to save the encrypted content.
3. **Decrypt File**
   - Input the name of the encrypted file.
   - Specify an output file name to save the decrypted content.
4. **Exit**
   - Exit the tool.

## Example Workflow
### 1. Generate a Key
Run the script and select option `1` to generate a key:
```bash
Enter your choice: 1
Key generated and saved as 'key.key'.
```

### 2. Encrypt a File
Prepare a text file named `example.txt` with the following content:
```
Hello, this is a test file for encryption.
```
Then, select option `2` to encrypt it:
```bash
Enter your choice: 2
Enter the file to encrypt: example.txt
Enter the output file name: encrypt_example.txt
File 'example.txt' encrypted and saved as 'encrypt_example.txt'.
```
The encrypted file `encrypt_example.txt` will contain like this:
```
gAAAAABneVxJ3-yHfj7S39-1xkmJ_Zslq-MPbeweRPwHrnDBFtRDmRy1ocnsaIx5bzBs1nRcJkYrJS9a4hHk8JKDSirxUkOShjhgZflWLgaijomFqVxy_Oo5lEQbUSozqPeNK0tZaACh
```

### 3. Decrypt the File
To decrypt the file, select option `3` and provide the encrypted file:
```bash
Enter your choice: 3
Enter the file to decrypt: encrypt_example.txt
Enter the output file name: decrypt_example.txt
File 'encrypt_example.txt' decrypted and saved as 'decrypt_example.txt'.
```
The decrypted file `decrypt_example.txt` will contain the original content:
```
Hello, this is a test file for encryption.
```

## Notes
- Ensure you keep the `key.key` file secure. Losing the key will make it impossible to decrypt your files.

## Troubleshooting
- **Key not found**: If you haven't generated a key, use option `1` to create one.
- **Invalid token**: Ensure the correct key is being used to decrypt the file.


## Author
- Created and maintained by **Sohag Chakraborty**  
  GitHub: [**@csesohag02**](https://github.com/csesohag02)
