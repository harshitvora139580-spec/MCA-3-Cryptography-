
p = int(input("Enter the value of p : "))
g = int(input("Enter the value of g : "))

alice = int(input("Enter Alice's Private Key: "))
bob = int(input("Enter Bob's Private Key: "))

alice_public = (g ** alice) % p
bob_public = (g ** bob) % p

print("Alice Public Key :", alice_public)
print("Bob Public Key   :", bob_public)

alice_shared = (bob_public ** alice) % p
bob_shared = (alice_public ** bob) % p

print("Alice Shared Secret :", alice_shared)
print("Bob Shared Secret   :", bob_shared)

