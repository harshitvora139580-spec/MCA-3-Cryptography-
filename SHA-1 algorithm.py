import hashlib

text=input("enter a string to generate hash:")
sha1_result=hashlib.sha1(text.encode())
print("\n--- SHA-1 HASH---")
print("SHA-1 (HEX):",sha1_result.hexdigest())
print("SHA-1 output size(in bites):",len(sha1_result.digest())*8)
