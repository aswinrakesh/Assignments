
from Crypto.Cipher import AES
obj = AES.new('1234567890123456', AES.MODE_CBC, 'This is an IV456')
print ("Input Plaintext")
message = raw_input()
x = len(message)
y = x%16
if ( y == 0):
        z = "\x10"*16
        message = message + z
else:
        message = message + (16-len(message)%16)*str(chr(16-len(message)%16))

ciphertext = obj.encrypt(message)
print ciphertext

message = raw_input()
x = len(message)
y = x%16
if ( y == 0):
        z = "\x10"*16
        message = message + z
else:
        message = message + (16-len(message)%16)*str(chr(16-len(message)%16))

ciphertext = obj.encrypt(message)
print ciphertext



            
