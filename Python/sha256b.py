def getHash():
    import hashlib
    m = hashlib.sha256()
    m.update(b"Chris")
    m.update(b" Stewart")
    print (m.hexdigest())
    return
getHash()

