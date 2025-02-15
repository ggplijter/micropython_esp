
# example of wifi_credential:
'''
SSID=***********
PASSWORD==***********
'''
with open("wifi_credentials", "r") as file:
    data = {}
    for line in file:
        key, value = line.strip().split("=", 1)  # Split at '='
        data[key] = value  # Store in a dictionary

message = f"{data['SSID']} {data['PASSWORD']}".encode()
padded_message = pad_message(message)
ciphertext = cipher.encrypt(padded_message)
print(ciphertext)



