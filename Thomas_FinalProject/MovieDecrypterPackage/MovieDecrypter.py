# Name: Dylan Moore
# email: moore4dl@mail.uc.edu
# Assignment Title: Final
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: The culmination of this semester and its teachings 
# Movie Decryption

from cryptography.fernet import Fernet
import json

#here we go
def Decrypter(): 
    '''
    This should decrypt things encyrpted using AES
    @param: json must be in project folder
    @returns: decrypted text
    '''
    file_path = 'file.json'

    with open(file_path, 'r') as file:
        data = json.load(file)
    print(data)
    key= "4g8xAE7lajIzp6UTyITiAGOYMSGzs5qKeMIdoT_js6U=" #Decryption key goes here
    name = "Thomas"
    token = data.get(name)
    
    fernet = Fernet(key.decrypt())
    decrypted_data = fernet.decrypt(token.encode())
    x = (decrypted_data.decode())
    return (x)
    print(x)
