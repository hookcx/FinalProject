#MovieDecrypter.py
# Name: Dylan Moore
# Email: moore4dl@mail.uc.edu
# Assignment Title: Final
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: The culmination of this semester and its teachings 
# Movie Decryption

from cryptography.fernet import Fernet
import json

#here we go
def decrypter():
    '''
    Decrypts a CSV file that is encrypted in AES
    @param: Specified key to decrypt selected
    @return: The decrypted string
    '''
    file_path = 'File.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    thomas_values = data.get("Thomas", [])
    key_str = "4g8xAE7lajIzp6UTyITiAGOYMSGzs5qKeMIdoT_js6U=" 
    key = key_str.encode()  # Decryption key in bytes
    if thomas_values:
        fernet = Fernet(key)
        decrypted_data_list = []
        for token in thomas_values:
            decrypted_data = fernet.decrypt(token.encode())
            x = decrypted_data.decode()
            decrypted_data_list.append(x)
        return print(decrypted_data_list)
    return print("Decrypter ERROR")  

#code to test and run decrypter
if __name__ == "__main__":
    decrypter()