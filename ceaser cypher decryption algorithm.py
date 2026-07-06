message = input("Enter the encrypted message: ")
shift = int(input("Enter the shift value: "))

for ch in message:
    print(chr((ord(ch) - 65 - shift) % 26 + 65), end="")
