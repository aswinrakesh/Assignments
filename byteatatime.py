from Crypto.Cipher import AES
import base64
obj = AES.new('1234567890123456', AES.MODE_ECB)
secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
secret = secret.decode('base64')

flag = ''
for k in range(1,(len(secret)/16)+2):
	for i in range(15, -1, -1):
		message = 'a'*i
		plaintext = message + secret
		plaintext = plaintext + (16-len(plaintext)%16)*str(chr(16-len(plaintext)%16))
		ciphertext = obj.encrypt(plaintext)
		for j in range(0,256):
			test = 'a'*i + flag + chr(j)
			test = test + (16-len(test)%16)*str(chr(16-len(test)%16))
			if (ciphertext[:16*k] == obj.encrypt(test)[:16*k]):
				flag = flag + chr(j)
				break
		print flag	


