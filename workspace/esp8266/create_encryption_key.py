
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

def print_encrypted(message):
    padded_message = pad_message(message)
    return cipher.encrypt(padded_message)

print(f"SSID={print_encrypted(data['SSID'].encode())}")
print(f"PASSWORD={print_encrypted(data['PASSWORD'].encode())}")







