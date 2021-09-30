import cryptography.fernet
import os

#test_key = b'jig-oaelcJoX2CtNdm6ZzFSmKy_yWXMMVDXpLBtMUFA='

class database_encryption:
    def __init__(self):
        self.key = os.getenv('ENC_KEY')
        self.fernet = cryptography.fernet.Fernet(self.key)

    def encrypt(self, content: str):
        return self.fernet.encrypt(content.encode())

test_crypt = database_encryption()
print(test_crypt.encrypt('hello world!'))