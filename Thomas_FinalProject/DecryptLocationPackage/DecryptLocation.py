def decrypt_location_data(index_list):
    decrypted_data = []
    with open('English.txt', 'r') as file:
        lines = file.readlines()
        for index in index_list:
            line_index = int(index)
            if 0 <= line_index < len(lines):
                decrypted_data.append(lines[line_index].strip())
            else:
                decrypted_data.append("[Index out of range]")
    return ' '.join(decrypted_data)


encrypted_data = [
        "42061",
        "44404",
        "28799",
        "298",
        "8848",
        "27781",
        "105654",
        "21723",
        "47096",
        "8021",
        "28420",
        "19312",
        "22147",
        "42049",
        "23887",
        "599",
        "105655",
        "24232",
        "19312",
        "9443"
    ]
decrypted_text = decrypt_location_data(encrypted_data)

#testing on Hello World
e =  ["20842", "46853"]
d = decrypt_location_data(e)

print(d)
print(decrypted_text)






