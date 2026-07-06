message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted = ""

for ch in message:
    encrypted += chr(ord(ch) + shift)

print("Encrypted message:", encrypted)
