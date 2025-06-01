import hashlib
print(hashlib.sha256(input("Enter secret question: >>> ").encode()).hexdigest())