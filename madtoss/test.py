from passlib.hash import pbkdf2_sha256
 
hash = pbkdf2_sha256.encrypt("password", rounds=20000)
print(pbkdf2_sha256.verify("password", hash))
