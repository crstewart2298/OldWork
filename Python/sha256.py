import hashlib
m = hashlib.sha256()
nonce = 256
found = 0
while found == 0:
    hh = str(nonce)+"::00004257eca8a841343564e90f7a19289fa604f9db307a709136c78fd580f540b196::Missouri"
    newHash = hashlib.sha256(hh.encode()).hexdigest()
    if newHash[:4] == '0000':
        found = 1
    nonce +=1
print("Block 1:")
print(newHash)
print("Nonce 1:")
print(nonce)
nonce2 = 256
found2 = 0
while found2 == 0:
    hh2 = str(nonce2)+"::" + newHash + "::Western"
    newHash2 = hashlib.sha256(hh2.encode()).hexdigest()
    if newHash2[:4] == '0000':
        found2 = 1
    nonce2 += 1
print("Block 2:")
print(newHash2)
print("Nonce 2:")
print(nonce2)
nonce3 = 256
found3 = 0
while found3 == 0:
    hh3 = str(nonce3)+"::" + newHash2 + "::State"
    newHash3 = hashlib.sha256(hh3.encode()).hexdigest()
    if newHash3[:4] == '0000':
        found3 = 1
    nonce3 += 1
print("Block 3:")
print(newHash3)
print("Nonce 3:")
print(nonce3)
nonce4 = 256
found4 = 0
while found4 == 0:
    hh4 = str(nonce4)+"::" + newHash3
    newHash4 = hashlib.sha256(hh4.encode()).hexdigest()
    if newHash4[:4] == '0000':
        found4 = 1
    nonce4 += 1
print("Block 4:")
print(newHash4)
print("Nonce 4")
print(nonce4)
